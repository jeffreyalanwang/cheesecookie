'''
Mary Johnson
Matthew Shimko
Jeffery Wang

Written by Mary Johnson
'''

from flask import Flask, render_template, url_for, request, redirect, send_from_directory, jsonify

# database
from flask_sqlalchemy import SQLAlchemy
from database_wrapper import DBAccess

# for file uploads
from glob import glob
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from werkzeug.security import safe_join

# sampling
import random

'''
array.db can be created/updated through the init_db.py file
python init_db.py
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///array.db'
app.config['UPLOAD_FOLDER'] = 'instance'
db = SQLAlchemy(app)

# Rules for database. Defining Columns.

CourseLanguage = db.Table(
    'CourseLanguage',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
    db.Column('language_id', db.Integer, db.ForeignKey('language.id')),
    
    db.PrimaryKeyConstraint('course_id', 'language_id')
)

CourseSoftware = db.Table(
    "CourseSoftware",
    db.Column("course_id", db.Integer, db.ForeignKey('course.id')),
    db.Column("software_id", db.Integer, db.ForeignKey('software.id')),
    db.PrimaryKeyConstraint('course_id', 'software_id')
) 

LanguageSoftware = db.Table(
    "LanguageSoftware",
    db.Column("language_id", db.Integer, db.ForeignKey('language.id')),
    db.Column("software_id", db.Integer, db.ForeignKey('software.id')),
    db.PrimaryKeyConstraint('language_id', 'software_id')
)

CourseRequiresCourse = db.Table(
    "CourseRequiresCourse",
    db.Column("course_id", db.ForeignKey('course.id')),
    db.Column("required_course_id", db.ForeignKey('course.id')),
    db.PrimaryKeyConstraint('course_id', 'required_course_id')
)

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    picture_url = db.Column(db.String)
    mod_status = db.Column(db.Boolean, nullable=False, default=False)

    owned_course = db.relationship('Course', uselist=False, backref='owned_by', lazy=True)
    owned_language = db.relationship('Language', uselist=False, backref='owned_by', lazy=True)
    owned_software = db.relationship('Software', uselist=False, backref='owned_by', lazy=True)

    owned_languageguide = db.relationship('LanguageGuide', uselist=False, backref='owned_by', lazy=True)
    owned_softwareguide = db.relationship('SoftwareGuide', uselist=False, backref='owned_by', lazy=True)


    def __repr__(self):
        return '<User: %r>' % self.name

class LanguageGuide(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    path = db.Column(db.String)

    language = db.relationship('Language', back_populates='guides') 

    user_id = db.Column(db.String, db.ForeignKey(User.id))
    
    def __repr__(self):
        return '<Language Guide: %r>' % self.id

class SoftwareGuide(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    path = db.Column(db.String)

    software = db.relationship('Software', back_populates='guides')

    user_id = db.Column(db.String, db.ForeignKey(User.id))

    def __repr__(self):
        return '<Software Guide: %r>' % self.id

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    course_code = db.Column(db.String(9), unique=True)
    credit_hours = db.Column(db.Integer)
    description = db.Column(db.String(1000))

    compatible_language = db.relationship('Language', secondary=CourseLanguage, backref='compatible_course')
    compatible_software = db.relationship('Software', secondary=CourseSoftware, backref='compatible_course')
    course_requires = db.relationship('Course', secondary=CourseRequiresCourse, primaryjoin=(CourseRequiresCourse.c.course_id == id), secondaryjoin=(CourseRequiresCourse.c.required_course_id == id), backref='prerequisite_of')

    user_id = db.Column(db.String, db.ForeignKey(User.id))

    def __repr__(self):
        return '<Course: %r>' % self.title

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    site_url = db.Column(db.String(200))
    download_url = db.Column(db.String(200))
    documentation_url = db.Column(db.String(200))
    description = db.Column(db.String(1000))

    guide_id = db.Column(db.Integer, db.ForeignKey(LanguageGuide.id))
    guides = db.relationship('LanguageGuide', back_populates='language', lazy=True)

    user_id = db.Column(db.String, db.ForeignKey(User.id))

    compatible_software = db.relationship('Software', secondary=LanguageSoftware, backref='compatible_language')

    def __repr__(self):
        return '<Language: %r>' % self.name

class Software(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    site_url = db.Column(db.String(200))
    download_url = db.Column(db.String(200))
    documentation_url = db.Column(db.String(200))
    description = db.Column(db.String(1000))

    guide_id = db.Column(db.Integer, db.ForeignKey(SoftwareGuide.id))
    guides = db.relationship('SoftwareGuide', back_populates='software', lazy=True)

    user_id = db.Column(db.String, db.ForeignKey(User.id))

    def __repr__(self):
        return '<Software: %r>' % self.name





# Access database through wrapper class
db_access = DBAccess(db, Course, Language, Software, User, LanguageGuide, SoftwareGuide)

# Defines actions with homepage, requesting the page
@app.route('/', methods=['GET'])
def index():
    # Display the index page.
    return render_template('index.html')

@app.route('/profile', methods=['GET'])
def userDetailsPage():
    return render_template('profile.html')

@app.route('/my_content', methods=['GET'])
def userContentPage():
    user_id = request.cookies.get('user')
    user = db_access.getUser(user_id)
    app.logger.info(user)
    if user:
        courses = user.owned_course
        languages = user.owned_language
        softwares = user.owned_software
    
    else: # and default for people who aren't logged in? idk if we needed this
        courses = db_access.allCourses()
        languages = db_access.allLanguages()
        softwares = db_access.allSoftwares()
    
    return render_template('my_content.html', softwares=softwares,languages=languages, courses=courses)

@app.route('/all_content', methods=['GET'])
def allContentPage():
    courses = db_access.allCourses()
    languages = db_access.allLanguages()
    softwares = db_access.allSoftwares()
    return render_template('all_content.html', softwares=softwares,languages=languages, courses=courses)

@app.route('/explore/', methods=['GET'])
def explorePage():
    courses = random.sample(db_access.allCourses(),3)
    languages = random.sample(db_access.allLanguages(),3)
    softwares = random.sample(db_access.allSoftwares(),3)
    return render_template('explore.html', softwares=softwares,languages=languages, courses=courses)

@app.route('/search', methods=['POST','GET'])
def search():

    # Used to dynamically list courses/languages/software
    all_course = db_access.allCourses(Course.id)
    all_language = db_access.allLanguages(Language.id)
    all_software = db_access.allSoftwares(Software.id)

    if request.method == 'POST':

        searchCourse = request.form.get('search_course', False)
        searchLanguage = request.form.get('search_language', False)
        searchSoftware = request.form.get('search_software', False)

        creditHours = request.form.get('credit_hours',False)

        compatibleLanguage = request.form.get('compatible_language',False)
        compatibleSoftware = request.form.get('compatible_software',False)
        compatibleCourse = request.form.get('compatible_course',False)

        prerequisiteCourse = request.form.get('prerequisite_course',False)
        requiresCourse = request.form.get('requires_course',False)
        
        try:
            
            # If course
            if searchCourse:
                courses = db_access.searchCourses(prerequisiteCourse=prerequisiteCourse,
                                        requiresCourse=requiresCourse,
                                        creditHours=creditHours,
                                        compatibleLanguage=compatibleLanguage,
                                        compatibleSoftware=compatibleSoftware)
            else: 
                courses = [] 

            # If lang
            if searchLanguage:
                languages = db_access.searchLanguages(compatibleCourse=compatibleCourse,
                                                    compatibleSoftware=compatibleSoftware)
            else: 
                languages = []

            # If software
            if searchSoftware:
                softwares = db_access.searchSoftwares(compatibleCourse=compatibleCourse,
                                                    compatibleLanguage=compatibleLanguage)
            else: 
                softwares = []

        
            return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software, courses=courses, languages=languages, softwares=softwares)
        except:
            return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software, err="There was an error with completing your search.")

    else:
        return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software)

@app.route('/about', methods=['GET'])
def about():
    # Display the about page.
    return render_template('about.html')

# Helper for database pages: get image
@app.route('/img/<path:folder>/<int:id>', methods=['GET'])
def img(folder, id=-1):
    folder_path = app.config['UPLOAD_FOLDER'] + '/img/' + folder + '/' + str(id) + '/'

    try:
        file_name = os.listdir(folder_path)[0]
    except (FileNotFoundError, IndexError):
        folder_path = app.config['UPLOAD_FOLDER'] + '/img/' + folder + '/placeholder/'
        file_name = os.listdir(folder_path)[0]
    
    return send_from_directory(folder_path, file_name)

def imgSave(folder, id, file, filename=None):
    if filename is None:
        filename = secure_filename(file.filename)
    
    folder_path = app.config['UPLOAD_FOLDER'] + '/img/' + folder + '/' + str(id) + '/'

    # create folder if needed
    Path(folder_path).mkdir(exist_ok=True)
    # delete existing image
    files = glob(folder_path + "*")
    for f in files:
        os.remove(f)
    # save image
    file.save(safe_join(folder_path, filename))

# Helper for profile: save new user
@app.post('/update_user')
def update_user():
    # receives POST request with fields: user_id, email, picture_url, name
    # save in database

    results = request.form
    db_access.setUser(id = results["user_id"],
                        name = results["name"],
                        email = results["email"],
                        picture_url = results["picture_url"])

    # return success
    return jsonify(success=True)

@app.context_processor
def add_user_details():
    user_id = request.cookies.get('user')
    user = db_access.getUser(user_id)
    if user:
        return dict(
            user_id = user_id,
            email = user.email,
            picture_url = user.picture_url,
            name = user.name,
            mod_status = user.mod_status
        )
    else:
        return dict()

# Database pages

@app.route('/course/<int:id>', methods=['GET'])
def coursePage(id):
    course = db_access.getCourse(id)
    client_user = db_access.getUser(request.cookies.get('user'))
    
    owner = course.owned_by
    if not owner: # no owner
        user_name = 'None'
        can_edit = True
    elif owner == client_user: # client is owner
        user_name = 'You'
        can_edit = True
    else: # owner is someone else
        user_name = owner.name
        can_edit = False

    if client_user and client_user.mod_status:
        can_edit = True

    return render_template('database/course.html', user=owner, user_name=user_name, editor=can_edit,
                           course=course,
                           languages=course.compatible_language, softwares=course.compatible_software, requires=course.course_requires)

@app.route('/course/<int:id>/edit', methods=['POST', 'GET'])
def courseEditPage(id):

    if request.method == 'POST':
        results = request.form
        db_access.setCourse(id,
                            title=results["title"],
                            course_code=results["course_code"],
                            credit_hours=int(results["credit_hours"]),
                            description=results["description"])
        db_access.setPrereq_Editor(id, results["course_ids"])
        db_access.setCourseLanguage_Editor(id, results["language_ids"])
        db_access.setCourseSoftware_Editor(id, results["software_ids"])

    all_course = db_access.allCourses(Course.id)
    all_language = db_access.allLanguages(Language.id)
    all_software = db_access.allSoftwares(Software.id)
    course = db_access.getCourse(id)
    return render_template('database_edit/course_edit.html', course=course, 
                           languages=course.compatible_language, softwares=course.compatible_software, requires=course.course_requires,
                           all_course=all_course, all_language=all_language, all_software=all_software)

@app.route('/language/<int:id>', methods=['GET'])
def languagePage(id):
    language = db_access.getLanguage(id)
    client_user = db_access.getUser(request.cookies.get('user'))
    
    owner = language.owned_by
    if not owner: # no owner
        user_name = 'None'
        can_edit = True
    elif owner == client_user: # client is owner
        user_name = 'You'
        can_edit = True
    else: # owner is someone else
        user_name = owner.name
        can_edit = False

    if client_user and client_user.mod_status:
        can_edit = True

    guides = language.guides
    return render_template('database/language.html', id=id, editor=can_edit, user_name=user_name, guides=guides, language=language,courses=language.compatible_course, softwares=language.compatible_software)
    
@app.route('/language/<int:id>/edit', methods=['POST', 'GET'])
def languageEditPage(id):

    if request.method == 'POST':
        results = request.form
        files = request.files
        db_access.setLanguage(id,
                            name=results["name"],
                            site_url=results["site_url"],
                            download_url=results["download_url"],
                            documentation_url=results["documentation_url"],
                            description=results["description"])
        if 'image' in files:
            imgFile = files['image']
            if imgFile.filename:
                imgSave('language', id, imgFile)
        db_access.setLanguageCourse_Editor(id, results["course_ids"])
        db_access.setLanguageSoftware_Editor(id, results["software_ids"])

    all_course = db_access.allCourses(Course.id)
    all_language = db_access.allLanguages(Language.id)
    all_software = db_access.allSoftwares(Software.id)
    language = db_access.getLanguage(id)
    return render_template('database_edit/language_edit.html', id=id, language=language,
                           courses=language.compatible_course, softwares=language.compatible_software,
                           all_course=all_course, all_language=all_language, all_software=all_software)

@app.route('/software/<int:id>', methods=['GET'])
def softwarePage(id):
    software = db_access.getSoftware(id)
    client_user = db_access.getUser(request.cookies.get('user'))
    
    owner = software.owned_by
    if not owner: # no owner
        user_name = 'None'
        can_edit = True
    elif owner == client_user: # client is owner
        user_name = 'You'
        can_edit = True
    else: # owner is someone else
        user_name = owner.name
        can_edit = False

    if client_user and client_user.mod_status:
        can_edit = True

    guides = software.guides
    return render_template('database/software.html', editor=can_edit, user_name=user_name, software=software, guides=guides, id=id, languages=software.compatible_language, courses=software.compatible_course)

@app.route('/software/<int:id>/edit', methods=['POST', 'GET'])
def softwareEditPage(id):

    if request.method == 'POST':
        results = request.form
        files = request.files
        db_access.setSoftware(id,
                            name=results["name"],
                            site_url=results["site_url"],
                            download_url=results["download_url"],
                            documentation_url=results["documentation_url"],
                            description=results["description"])
        if 'image' in files:
            imgFile = files['image']
            if imgFile.filename:
                imgSave('software', id, imgFile)
        db_access.setSoftwareLanguage_Editor(id, results["language_ids"])
        db_access.setSoftwareCourse_Editor(id, results["course_ids"])

    all_course = db_access.allCourses(Course.id)
    all_language = db_access.allLanguages(Language.id)
    all_software = db_access.allSoftwares(Software.id)
    software = db_access.getSoftware(id)
    return render_template('database_edit/software_edit.html', id=id, software=software,
                            languages=software.compatible_language, courses=software.compatible_course,
                            all_course=all_course, all_language=all_language, all_software=all_software)

# e.g. /software/1/guide/1
# type can be language or software.
@app.route('/<path:type>/<int:id>/guide/<int:guide_id>', methods=['GET'])
def guidePage(type, id, guide_id):
    
    match type:
        case "software":
            parent_db = Software
            target_db = SoftwareGuide
        case "language":
            parent_db = Language
            target_db = LanguageGuide
    guide = target_db.query.get_or_404(guide_id)

    owner = guide.owned_by
    client_user = db_access.getUser(request.cookies.get('user'))
    if not owner: # no owner
        user_name = 'None'
        can_edit = True
    elif owner == client_user: # client is owner
        user_name = 'You'
        can_edit = True
    else: # owner is someone else
        user_name = owner.name
        can_edit = False

    data = dict(guide = guide)

    data['title'] = guide.name
    data['guideText'] = guide.path
    data['user_name'] = user_name
    
    data['parent_href'] = '/{type}/{id}'.format(type=type, id=id)
    data['parent_name'] = parent_db.query.get_or_404(id).name

    data['editor'] = can_edit

    return render_template('database/guide.html', **data)

@app.route('/<path:type>/<int:id>/guide/<int:guide_id>/edit', methods=['POST', 'GET'])
def guideEditPage(type, id, guide_id):

    match type:
        case "software":
            parent_db = Software
            target_db = SoftwareGuide
        case "language":
            parent_db = Language
            target_db = LanguageGuide
    guide = target_db.query.get_or_404(guide_id)

    if request.method == 'POST':
        results = request.form
        guide.name = results["title"]
        guide.path = results["html_content"]
        db.session.commit()

    data = dict(guide = guide)

    data['title'] = guide.name
    if guide.path:
        data['guideText'] = guide.path.replace('"', '\\"')
    else:
        data['guideText'] = ''
    
    data['parent_name'] = parent_db.query.get_or_404(id).name

    return render_template('database_edit/guide_edit.html', **data)


@app.route('/<path:type>/new', methods=['GET'])
@app.route('/<path:parent_type>/<path:parent_id>/<path:type>/new', methods=['GET'])
def newDatabaseContent(type, parent_type=None, parent_id=None):

    match type:
        case "course":
            target_db = Course
            editPage = courseEditPage
        case "software":
            target_db = Software
            editPage = softwareEditPage
        case "language":
            target_db = Language
            editPage = languageEditPage
        case "guide":
            match parent_type:
                case "software":
                    target_db = SoftwareGuide
                case "language":
                    target_db = LanguageGuide
            editPage = guideEditPage
        case _:
            app.logger.error('Bad content type')


    # create new item in target db
    if type == "guide":
        newRow = target_db()
        match parent_type:
            case "software":
                newRow.software.append(db_access.getSoftware(parent_id))
            case "language":
                newRow.language.append(db_access.getLanguage(parent_id))
    elif type == "course":
        newRow = target_db(title="New " + type.capitalize() + " Entry") # Title is not nullable.
    else:
        newRow = target_db(name="New " + type.capitalize() + " Entry") # Name is not nullable.
    db.session.add(newRow)

    # set user id of the created content
    owner_id = request.cookies.get('user')
    newRow.owned_by = db_access.getUser(owner_id) # could set to None if user is not signed in

    db.session.commit()
    
    # get id of new row
    id = newRow.id
    

    # redirect user to edit new page
    if type == "guide":
        return redirect(url_for(editPage.__name__, type=parent_type, id=parent_id, guide_id=id))
    else:
        return redirect(url_for(editPage.__name__, id=id))


# Run in debug mode so errors get displayed
if __name__ == "__main__":
    app.run(debug=True)
