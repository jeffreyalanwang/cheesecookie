# wrapper class for SQLAlchemy database
class DBAccess:
    def __init__(self, db, CourseModel, LanguageModel, SoftwareModel):
        self.db = db
        self.Course = CourseModel
        self.Language = LanguageModel
        self.Software = SoftwareModel

    # Add, set, get, search database entries
    # delete support not implemented

    def addCourse(self, title=None, course_code=None, credit_hours=None, description=None):
        course = self.Course(title=title, course_code=course_code, credit_hours=credit_hours, description=description)
        self.db.session.add(course)
        self.db.session.commit()

    def setCourse(self, id, title, course_code, credit_hours, description):
        course = self.db.session.get(self.Course, id)

        course.title = title
        course.course_code = course_code
        course.credit_hours = credit_hours
        course.description = description
        
        self.db.session.commit()

    def getCourse(self, id):
        return self.Course.query.get_or_404(id)

    def allCourses(self, order=None):
        query = self.Course.query

        if order:
            query = query.order_by(order)

        return query.all()
    
    def searchCourses(self, prerequisiteCourse=0, requiresCourse=0, creditHours=0, compatibleLanguage=0, compatibleSoftware=0):
        courses = self.Course.query

        if int(prerequisiteCourse) > 0:
            prereq = self.Course.query.filter_by(id=prerequisiteCourse).first()
            courses = courses.filter(self.Course.prerequisite_of.contains(prereq))

        if int(requiresCourse) > 0:
            required = self.Course.query.filter_by(id=requiresCourse).all()
            coursesQ = self.Course.query.filter_by(id=0)
            for req in required:
                coursesQ = coursesQ.union(courses.filter(self.Course.course_requires.contains(req)))
            courses = courses.intersect(coursesQ)

        if int(creditHours) > 0:
            courses = courses.filter_by(credit_hours=creditHours)
        
        if int(compatibleLanguage) > 0:
            courses = courses.join(self.Course.compatible_language).filter(self.Language.id==compatibleLanguage)

        if int(compatibleSoftware) > 0:
            courses = courses.join(self.Course.compatible_software).filter(self.Software.id==compatibleSoftware)
            
        return courses.order_by(self.Course.id).all()

    def addLanguage(self, name=None, site_url=None, download_url=None, documentation_url=None, description=None):
        language = self.Language(name=name, site_url=site_url, download_url=download_url, documentation_url=documentation_url, description=description)
        self.db.session.add(language)
        self.db.session.commit()

    def setLanguage(self, id, name, site_url, download_url, documentation_url, description):
        language = self.db.session.get(self.Language, id)

        language.name = name
        language.site_url = site_url
        language.download_url = download_url
        language.documentation_url = documentation_url
        language.description = description

        self.db.session.commit()

    def getLanguage(self, id):
        return self.Language.query.get_or_404(id)

    def allLanguages(self, order=None):
        query = self.Language.query

        if order:
            query = query.order_by(order)

        return query.all()
    
    def searchLanguages(self, compatibleCourse=0, compatibleSoftware=0):
        languages = self.Language.query

        if int(compatibleCourse) > 0:
            languages = languages.join(self.Language.compatible_course).filter(self.Course.id==compatibleCourse)

        if int(compatibleSoftware) > 0:
            languages = languages.join(self.Language.compatible_software).filter(self.Software.id==compatibleSoftware)

        return languages.order_by(self.Language.id).all()

    def addSoftware(self, name=None, site_url=None, download_url=None, documentation_url=None, description=None):
        language = self.Language(name=name, site_url=site_url, download_url=download_url, documentation_url=documentation_url, description=description)
        self.db.session.add(language)
        self.db.session.commit()

    def setSoftware(self, id, name, site_url, download_url, documentation_url, description):
        software = self.db.session.get(self.Software, id)

        software.name = name
        software.site_url = site_url
        software.download_url = download_url
        software.documentation_url = documentation_url
        software.description = description

        self.db.session.commit()

    def getSoftware(self, id):
        return self.Software.query.get_or_404(id)

    def allSoftwares(self, order=None):
        query = self.Software.query

        if order:
            query = query.order_by(order)

        return query.all()
    
    def searchSoftwares(self, compatibleCourse=0, compatibleLanguage=0):
        softwares = self.Software.query

        if int(compatibleLanguage) > 0:
            softwares = softwares.join(self.Language.compatible_software).filter(self.Software.id==compatibleLanguage)

        if int(compatibleCourse) > 0:
            softwares = softwares.join(self.Course.compatible_software).filter(self.Course.id==compatibleCourse)

        return softwares.order_by(self.Software.id).all()
    
    # add relationships between database entries
    # delete/edit support not implemented

    def addCoursePrerequisite(self, course_id, prerequisite_id):
        course = self.db.session.get(self.Course, course_id)
        prerequisite = self.db.session.get(self.Course, prerequisite_id)

        prerequisite.prerequisite_of.append(course)

        self.db.session.commit()

    def addCourseLanguage(self, course_id, language_id):
        course = self.db.session.get(self.Course, course_id)
        language = self.db.session.get(self.Course, language_id)

        course.compatible_language.append(language)

        self.db.session.commit()

    def addLanguageCourse(self, language_id, course_id):
        self.addCourseLangage(course_id, language_id)

    def addCourseSoftware(self, course_id, software_id):
        course = self.db.session.get(self.Course, course_id)
        software = self.db.session.get(self.Course, software_id)

        course.compatible_software.append(software)

        self.db.session.commit()

    def addSoftwareCourse(self, software_id, course_id):
        self.addCourseSoftware(course_id, software_id)

    def addLanguageSoftware(self, language_id, software_id):
        language = self.db.session.get(self.Course, language_id)
        software = self.db.session.get(self.Course, software_id)

        language.compatible_software.append(software)

        self.db.session.commit()

    def addSoftwareLanguage(self, software_id, language_id):
        self.addLanguageSoftware(language_id, software_id)