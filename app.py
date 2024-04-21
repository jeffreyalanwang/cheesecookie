'''
Mary Johnson
Matthew Shimko
Jeffery Wang

Written by Mary Johnson
'''

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from database_wrapper import DBAccess
import random

'''
array.db can be created/updated through the init_db.py file
python init_db.py
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///array.db'
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
    # I don't have time to figure out how to make this work. Next Sprint
    # db.Column("section_num", db.String(200)),
    # db.Column("installation_url", db.String(200)),
    # db.Column("installation_text", db.String(200)),
    db.PrimaryKeyConstraint('course_id', 'software_id') #, 'section_num')
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

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    course_code = db.Column(db.String(9), nullable=False)
    credit_hours = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(1000))

    compatible_language = db.relationship('Language', secondary=CourseLanguage, backref='compatible_course')
    compatible_software = db.relationship('Software', secondary=CourseSoftware, backref='compatible_course')
    course_requires = db.relationship('Course', secondary=CourseRequiresCourse, primaryjoin=(CourseRequiresCourse.c.course_id == id), secondaryjoin=(CourseRequiresCourse.c.required_course_id == id), backref='prerequisite_of')

    def __repr__(self):
        return '<Course: %r>' % self.title

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    site_url = db.Column(db.String(200))
    download_url = db.Column(db.String(200))
    documentation_url = db.Column(db.String(200))
    description = db.Column(db.String(1000))

    compatible_software = db.relationship('Software', secondary=LanguageSoftware, backref='compatible_language')

    def __repr__(self):
        return '<Language: %r>' % self.name

class Software(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    site_url = db.Column(db.String(200))
    download_url = db.Column(db.String(200))
    documentation_url = db.Column(db.String(200))
    description = db.Column(db.String(1000))

    def __repr__(self):
        return '<Software: %r>' % self.name

# Access database through wrapper class
db_access = DBAccess(db, Course, Language, Software)

# Defines actions with homepage, requesting the page
@app.route('/', methods=['GET'])
def index():
    # Display the index page.
    return render_template('index.html')

@app.route('/my_content', methods=['GET'])
def contentListPage():
    return render_template('explore.html', softwares=softwares,languages=languages, courses=courses)

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
        # TODO gather categories/search terms/narrowing factors/

        searchCourse = request.form.get('search_course', False)
        searchLanguage = request.form.get('search_language', False)
        searchSoftware = request.form.get('search_software', False)

        creditHours = request.form.get('credit_hours',False)

        compatibleLanguage = request.form.get('compatible_language',False)
        compatibleSoftware = request.form.get('compatible_software',False)
        compatibleCourse = request.form.get('compatible_course',False)

        prerequisiteCourse = request.form.get('prerequisite_course',False)
        requiresCourse = request.form.get('requires_course',False)
        

        # TODO perform the SQL queries to get the results list
        
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

        try:
            return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software, courses=courses, languages=languages, softwares=softwares) #  TODO Add a # to direct to top of results
        except:
            return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software, err="There was an error with completing your search.")

    else:
        return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software)


@app.route('/about', methods=['GET'])
def about():
    # Display the about page.
    return render_template('about.html')

# Database pages

@app.route('/course/<int:id>', methods=['GET'])
def coursePage(id):
    course = db_access.getCourse(id)
    return render_template('database/course.html', course=course, languages=course.compatible_language, softwares=course.compatible_software, requires=course.course_requires)

@app.route('/course/<int:id>/edit', methods=['POST', 'GET'])
def courseEditPage(id):

    if request.method == 'POST':
        results = request.form
        db_access.setCourse(id,
                            title=results["title"],
                            course_code=results["course_code"],
                            credit_hours=int(results["credit_hours"]),
                            description=results["description"])

    course = db_access.getCourse(id)
    return render_template('database_edit/course_edit.html', course=course,languages=course.compatible_language, softwares=course.compatible_software, requires=course.course_requires)

@app.route('/language/<int:id>', methods=['GET'])
def languagePage(id):
    language = db_access.getLanguage(id)
    return render_template('database/language.html', language=language,courses=language.compatible_course, softwares=language.compatible_software)
    
@app.route('/language/<int:id>/edit', methods=['POST', 'GET'])
def languageEditPage(id):

    if request.method == 'POST':
            results = request.form
            db_access.setLanguage(id,
                                name=results["name"],
                                site_url=results["site_url"],
                                download_url=results["download_url"],
                                documentation_url=results["documentation_url"],
                                description=results["description"])

    language = db_access.getLanguage(id)
    return render_template('database_edit/language_edit.html', language=language,courses=language.compatible_course, softwares=language.compatible_software)

@app.route('/software/<int:id>', methods=['GET'])
def softwarePage(id):
    software = db_access.getSoftware(id)
    return render_template('database/software.html', software=software,languages=software.compatible_language, courses=software.compatible_course)

@app.route('/software/<int:id>/edit', methods=['POST', 'GET'])
def softwareEditPage(id):

    if request.method == 'POST':
            results = request.form
            db_access.setSoftware(id,
                                name=results["name"],
                                site_url=results["site_url"],
                                download_url=results["download_url"],
                                documentation_url=results["documentation_url"],
                                description=results["description"])

    software = db_access.getSoftware(id)
    return render_template('database_edit/software_edit.html', software=software,languages=software.compatible_language, courses=software.compatible_course)

# e.g. /software/1/guide/1
# type can be language or software.
# to simplify, we can change the guide feature to only work for software.
@app.route('/<path:type>/<int:id>/guide/<int:guide_id>', methods=['GET'])
def guidePage(type, id, guide_id):
    # TODO setup this part of database
    if type == "software":
        guide = Software.query.get_or_404(id) # change to get correct guide instead of software itself
    if type == "language":
        guide = Language.query.get_or_404(id) # change to get correct guide instead of software itself

    return render_template('database/guide.html', guide=guide)

@app.route('/<path:type>/<int:id>/guide/<int:guide_id>/edit', methods=['POST', 'GET'])
def guideEditPage(type, id, guide_id):
    # TODO setup this part of database
    guide = None

    if request.method == 'POST':
            results = request.form
            # TODO save content in database

    return render_template('database_edit/guide_edit.html', guide=guide)

# Run in debug mode so errors get displayed
if __name__ == "__main__":
    app.run(debug=True)