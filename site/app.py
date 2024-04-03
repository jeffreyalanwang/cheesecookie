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

# I don't have time to figure out how to make this work. Next Sprint
'''
CourseRequiresCourse = db.Table(
    "CourseRequiresCourse",
    db.Column("course_id", db.ForeignKey('course.id')),
    db.Column("required_course_id", db.ForeignKey('course.id')),
    db.PrimaryKeyConstraint('course_id', 'required_course_id')
)
'''

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    course_code = db.Column(db.String(9), nullable=False)
    credit_hours = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(400))

    compatible_language = db.relationship('Language', secondary=CourseLanguage, backref='compatible_course')
    compatible_software = db.relationship('Software', secondary=CourseSoftware, backref='compatible_course')
    
    # I don't have time to figure out how to make this work. Next Sprint
    # course_requires = db.relationship('Course', secondary=CourseRequiresCourse, backref='prerequisite')

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
    if request.method == 'POST':
        # TODO gather categories/search terms/narrowing factors/

        searchCourse = request.form.get('search_course', False)
        searchLanguage = request.form.get('search_language', False)
        searchSoftware = request.form.get('search_software', False)

        creditHours = request.form.get('credit_hours',False)

        # I don't have time to figure out how to make this work. Next Sprint
        '''
        compatibleLanguage = request.form.get('compatible_language',False)
        compatibleSoftware = request.form.get('compatible_software',False)
        compatibleCourse = request.form.get('compatible_course',False)
        '''

        # TODO perform the SQL queries to get the results list
        
        # If course
        if searchCourse:
            courses = Course.query

            # I don't have time to figure out how to make this work. Next Sprint
            '''
            if int(compatibleLanguage) > 0:
                courses.filter_by(compatible_language=compatibleLanguage)

            if int(compatibleSoftware) > 0:
                print()
            '''

            if int(creditHours) > 0:
                courses = courses.filter_by(credit_hours=creditHours)
            courses = courses.order_by(Course.id).all()
        else: 
            courses = [] 

        # If lang
        if searchLanguage:
            languages = Language.query

            # I don't have time to figure out how to make this work. Next Sprint
            '''
            if compatibleCourse:
                print()
            if compatibleSoftware:
                print()
            '''

            languages = languages.order_by(Language.id).all()
        else: 
            languages = []

        # If software
        if searchSoftware:
            softwares = Software.query

            # I don't have time to figure out how to make this work. Next Sprint
            '''
            if compatibleCourse:
                print()
            if compatibleLanguage:
                print()
            '''

            softwares = softwares.order_by(Software.id).all()
        else: 
            softwares = []


        try:
            return render_template('search.html', courses=courses, languages=languages, softwares=softwares) #  TODO Add a # to direct to top of results
        except:
            return render_template('search.html', err="There was an error with completing your search.")

    else:
        return render_template('search.html')


@app.route('/course/<int:id>', methods=['GET'])
def coursePage(id):
    #  TODO Get the entry for that ID in course table
    course = Course.query.get_or_404(id)
    #  TODO Render with that info
    return render_template('course.html', course=course)


@app.route('/language/<int:id>', methods=['GET'])
def languagePage(id):
    #  TODO Get the entry for that ID in language table
    language = Language.query.get_or_404(id)
    #  TODO Render with that info
    return render_template('language.html', language=language)
    

@app.route('/software/<int:id>', methods=['GET'])
def softwarePage(id):
    #  TODO Get the entry for that ID in software database
    software = Software.query.get_or_404(id)
    #  TODO Render with that info
    return render_template('software.html', software=software)



# Run in debug mode so errors get displayed
if __name__ == "__main__":
    app.run(debug=True)