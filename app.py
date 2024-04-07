'''
Mary Johnson
Matthew Shimko
Jeffery Wang

Written by Mary Johnson
'''

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

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
    description = db.Column(db.String(400))

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
    description = db.Column(db.String(400))

    compatible_software = db.relationship('Software', secondary=LanguageSoftware, backref='compatible_language')

    def __repr__(self):
        return '<Language: %r>' % self.name

class Software(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    site_url = db.Column(db.String(200))
    download_url = db.Column(db.String(200))
    documentation_url = db.Column(db.String(200))
    description = db.Column(db.String(400))

    def __repr__(self):
        return '<Software: %r>' % self.name





# Defines actions with homepage, requesting the page
@app.route('/', methods=['GET'])
def index():
    # Display the index page.
    return render_template('index.html')


@app.route('/search', methods=['POST','GET'])
def search():

    # Used to dynamically list courses/languages/software
    all_course = Course.query.order_by(Course.id).all()
    all_language = Language.query.order_by(Language.id).all()
    all_software = Software.query.order_by(Software.id).all()

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
            courses = Course.query

            if int(prerequisiteCourse) > 0:
                prereq = Course.query.filter_by(id=prerequisiteCourse).first()
                courses = courses.filter(Course.prerequisite_of.contains(prereq))

            if int(requiresCourse) > 0:
                required = Course.query.filter_by(id=requiresCourse).all()
                coursesQ = Course.query.filter_by(id=0)
                for req in required:
                    coursesQ = coursesQ.union(courses.filter(Course.course_requires.contains(req)))
                courses = courses.intersect(coursesQ)


            if int(creditHours) > 0:
                courses = courses.filter_by(credit_hours=creditHours)
            
            if int(compatibleLanguage) > 0:
                courses = courses.join(Course.compatible_language).filter(Language.id==compatibleLanguage)

            if int(compatibleSoftware) > 0:
                courses = courses.join(Course.compatible_software).filter(Software.id==compatibleSoftware)
            
        

            courses = courses.order_by(Course.id).all()
        else: 
            courses = [] 

        # If lang
        if searchLanguage:
            languages = Language.query

            if int(compatibleCourse) > 0:
                languages = languages.join(Language.compatible_course).filter(Course.id==compatibleCourse)

            if int(compatibleSoftware) > 0:
                languages = languages.join(Language.compatible_software).filter(Software.id==compatibleSoftware)

            languages = languages.order_by(Language.id).all()
        else: 
            languages = []

        # If software
        if searchSoftware:
            softwares = Software.query

            if int(compatibleCourse) > 0:
                softwares = softwares.join(Course.compatible_software).filter(Software.id==compatibleSoftware)

            if int(compatibleLanguage) > 0:
                softwares = softwares.join(Language.compatible_course).filter(Course.id==compatibleCourse)

            softwares = softwares.order_by(Software.id).all()
        else: 
            softwares = []


        try:
            return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software, courses=courses, languages=languages, softwares=softwares) #  TODO Add a # to direct to top of results
        except:
            return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software, err="There was an error with completing your search.")

    else:
        return render_template('search.html', all_course=all_course, all_language=all_language, all_software=all_software)


@app.route('/course/<int:id>', methods=['GET'])
def coursePage(id):
    #  TODO Get the entry for that ID in course table
    course = Course.query.get_or_404(id)
    #  TODO Render with that info
    return render_template('course.html', course=course,languages=course.compatible_language, softwares=course.compatible_software, requires=course.course_requires)


@app.route('/language/<int:id>', methods=['GET'])
def languagePage(id):
    #  TODO Get the entry for that ID in language table
    language = Language.query.get_or_404(id)
    #  TODO Render with that info
    return render_template('language.html', language=language,courses=language.compatible_course, softwares=language.compatible_software)
    

@app.route('/software/<int:id>', methods=['GET'])
def softwarePage(id):
    #  TODO Get the entry for that ID in software database
    software = Software.query.get_or_404(id)
    #  TODO Render with that info
    return render_template('software.html', software=software,languages=software.compatible_language, courses=software.compatible_course)



# Run in debug mode so errors get displayed
if __name__ == "__main__":
    app.run(debug=True)