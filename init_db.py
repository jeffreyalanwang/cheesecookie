from app import db
from app import *

db.drop_all()
db.create_all()

C1 = Course(title='Introduction to Computer Systems', course_code='ITSC 2181', credit_hours='4', description='Introduction to computer system abstractions reflected in programming languages, operating systems, architectures, and networks.')
C2 = Course(title='Data Structures and Algorithms', course_code='ITSC 2214', credit_hours='3', description='A study of the theory and implementation of abstract data types (ADTs) including stacks, queues, and both general purpose and specialized trees and graphs.')
C3 = Course(title='Software Engineering', course_code='ITSC 3155', credit_hours='3', description='An introduction to software engineering, which advances the study and application of engineering principles, methods, and techniques that can help us to improve the process of creating software as well as the resulting software products.')

L1 = Language(name='Python', site_url='https://www.python.org/', download_url='https://www.python.org/downloads/', documentation_url='https://docs.python.org/')
L2 = Language(name='C', site_url='https://www.open-std.org/jtc1/sc22/wg14/', description='')

S1 = Software(name='Visual Studio Code', site_url='https://code.visualstudio.com/', download_url='https://code.visualstudio.com/download', documentation_url='https://code.visualstudio.com/docs')

C1.compatible_language.append(L2)

C1.compatible_software.append(S1)
C2.compatible_software.append(S1)

L1.compatible_software.append(S1)

db.session.add_all([C1,C2,C3])
db.session.add_all([L1,L2])
db.session.add_all([S1])

db.session.commit()
