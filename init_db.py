from app import db
from app import *

db.drop_all()
db.create_all()

C1 = Course(title='Introduction to Computer Systems', course_code='ITSC 2181', credit_hours='4', description='Introduction to computer system abstractions reflected in programming languages, operating systems, architectures, and networks.')
C2 = Course(title='Data Structures and Algorithms', course_code='ITSC 2214', credit_hours='3', description='A study of the theory and implementation of abstract data types (ADTs) including stacks, queues, and both general purpose and specialized trees and graphs.')
C3 = Course(title='Software Engineering', course_code='ITSC 3155', credit_hours='3', description='An introduction to software engineering, which advances the study and application of engineering principles, methods, and techniques that can help us to improve the process of creating software as well as the resulting software products.')
C4 = Course(title='Introduction to Computer Science I', course_code='ITSC 1212', credit_hours='4', description='Introduction to basic computer literacy, computational thinking and problem-solving using a high level programming language. Programming concepts will be introduced and applied, including: operators; data types; variables, constants, and literals; expressions; control structures and program flow; basic data structures such as arrays, lists, and maps; defining and using functions; file input/output. This is an introductory programming course for non-CS majors and the first course for students interested in pursuing a computer science major or related minor.')
C5 = Course(title='Introduction to Computer Science II', course_code='ITSC 1213', credit_hours='4', description='Reinforcement of computational thinking and problem-solving skills. Application of object-oriented programming principles including class design, encapsulation, inheritance, polymorphism, interfaces, abstract classes, aggregation and association. Additional topics include version control, use of debuggers and exception handling. This is the second course for students interested in pursuing a computer science major or related minor.')
C6 = Course(title='Computing Professionals', course_code='ITSC 1600', credit_hours='2', description='An introduction to becoming a computing professional. Students learn about setting goals, defining their dream career, becoming a part of the University, planning coursework, building network, managing time, and working in a team.  Additionally, guest speakers and industry panels discuss and explain aspects of a professional career in IT-related fields.  Throughout the course, students build a professional profile including their goals, values, dream career, student organizations, coding skills, communication skills, curriculum plan, professional network, a team TED talk, resume, and a 30-second elevator pitch.')
C7 = Course(title='Computer Science Program, Identity, Career', course_code='ITSC 2600', credit_hours='2', description='Introduces the computer science program and develops a student’s identity and career preparedness. Students learn about the program’s progression and graduation requirements, discuss concentration choices, and make curriculum plans. The course stimulates professional identity building emphasizing ethical uses of technology, diversity, career paths, and research.  Course outcomes emphasize an inclusive culture dedicated to student success and equity in the field of computing.')
C8 = Course(title='Logic and Algorithms', course_code='ITSC 2175', credit_hours='3', description='A study of discreet mathematical concepts.  Introduction to propositional calculus, predicate calculus, algorithms, logic functions, finite-state machines; and logic design.')
C9 = Course(title='Introduction to Operating Systems and Networking', course_code='ITSC 3146', credit_hours='3', description='Introduces the fundamentals of operating systems together with the basics of networking and communications.  Topics include: processes, thread, scheduling, cache, memory management, file systems, interprocess communication, network architecture and protocols, HTTP, MAC, IP, TCP/UPD, and Internet routing. ')
C10 = Course(title='Computers and Their Impact on Society', course_code='ITSC 3688', credit_hours='3', description='A study of current topics (software piracy, hacking, professional conduct) in computer science and the impact of computers on various subsets (home, government, and education) of society.')
C11 = Course(title='Introduction to Computer Networks', course_code='ITCS 3166', credit_hours='3', description='Internet architecture and protocols. Distributed vs. centralized processing. Data communications; speed; capacity; media, protocols. Network architectures. Evaluation of alternatives. Case studies.')
C12 = Course(title='Database Design and Implementation', course_code='ITCS 3160', credit_hours='3', description='Logical and physical database organization, data models, design issues, and secondary storage considerations. Emphasis on actual participation in the design and implementation of databases.')
C13 = Course(title='Intro to Video Game Design and Development', course_code='ITCS 4230', credit_hours='3', description='Basic concepts and techniques for electronic game design and development. Topics include: game history and genres, game design teams and processes, what makes a game fun, level and model design, game scripting and programming including computer graphics and animation, artificial intelligence, industry issues, and gender and games.')
C14 = Course(title='Web-Based Application Design and Development', course_code='ITIS 3135', credit_hours='3', description='Design and programming concepts for developing interactive web based applications: HTML, CSS, the Document Object Model (DOM), event-driven programming, client side scripting, and web security considerations.')
C15 = Course(title='Human-Centered Design', course_code='ITIS 3130', credit_hours='3', description='An introduction to methods and practice of human-centered design for interactive systems.  Topics include: design principles, need finding, design prototypes, and evaluation of interaction designs so that interactive systems are compatible with human capabilities and expectations.  Students learn to work in design teams and write project reports.')

L1 = Language(name='Python', site_url='https://www.python.org/', download_url='https://www.python.org/downloads/', documentation_url='https://docs.python.org/')
L2 = Language(name='C', site_url='https://www.open-std.org/jtc1/sc22/wg14/', description='')
L3 = Language(name='RISC-V', site_url='https://riscv.org', documentation_url='https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf', description='RISC-V is an open standard Instruction Set Architecture (ISA) enabling a new era of processor innovation through open collaboration')
L4 = Language(name='SQL')
L5 = Language(name='HTML')
L6 = Language(name='CSS')
L7 = Language(name='JavaScript', documentation_url='https://developer.mozilla.org/en-US/docs/Web/JavaScript', description='JavaScript is a lightweight interpreted programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript is a prototype-based, multi-paradigm, single-threaded, dynamic language, supporting object-oriented, imperative, and declarative styles.')
L8 = Language(name='Java', site_url='https://www.java.com/en/', download_url='https://www.java.com/en/download/', documentation_url='https://docs.oracle.com/en/java/', description='Java is a programming language and computing platform first released by Sun Microsystems in 1995. It has evolved from humble beginnings to power a large share of today’s digital world, by providing the reliable platform upon which many services and applications are built. New, innovative products and digital services designed for the future continue to rely on Java, as well.')
L9 = Language(name='C+')
L10 = Language(name='C++')
L11 = Language(name='GML', description='GML is a programming language used in Game Maker Studio. It takes elements from Java, Python, and C#.')
L12 = Language(name='C#', documentation_url='https://learn.microsoft.com/en-us/dotnet/csharp/', description='C# is a cross-platform general purpose language that makes developers productive while writing highly performant code. With millions of developers, C# is the most popular .NET language.')

S1 = Software(name='Visual Studio Code', site_url='https://code.visualstudio.com/', download_url='https://code.visualstudio.com/download', documentation_url='https://code.visualstudio.com/docs')
S2 = Software(name='Wireshark')
S3 = Software(name='Oracle Virtualbox')
S4 = Software(name='Ubuntu')
S5 = Software(name='Imunes', site_url='https://imunes.net/', download_url='https://imunes.net/download', documentation_url='https://imunes.net/dl/guide/')
S6 = Software(name='Game Maker Studio 2', site_url='https://gamemaker.io/en', download_url='https://gamemaker.io/en/download', documentation_url='https://gamemaker.io/en/tutorials', description='A game engine that is is primarily focused on the development of 2D Games')
S7 = Software(name='MySQL Workbench', site_url='https://www.mysql.com/products/workbench/', download_url='https://dev.mysql.com/downloads/workbench/', documentation_url='https://dev.mysql.com/doc/workbench/en/', description='MySQL Workbench is a unified visual tool for database architects, developers, and DBAs. MySQL Workbench provides data modeling, SQL development, and comprehensive administration tools for server configuration, user administration, backup, and much more. MySQL Workbench is available on Windows, Linux and Mac OS X.')
S8 = Software(name='Unity', site_url='https://unity.com/', download_url='https://unity.com/pricing', documentation_url='https://docs.unity.com/', description='Unity’s real-time 3D development engine lets artists, designers, and developers collaborate to create amazing immersive and interactive experiences. You can work on Windows, Mac, and Linux.')

C1.compatible_language.append(L2)
C3.compatible_language.append(L1)

C1.compatible_software.append(S1)
C3.compatible_software.append(S1)

L1.compatible_software.append(S1)

C1.prerequisite_of.append(C9)

C2.prerequisite_of.append(C9)
C2.prerequisite_of.append(C3)

C4.prerequisite_of.append(C8)
C4.prerequisite_of.append(C1)
C4.prerequisite_of.append(C5)

C5.prerequisite_of.append(C2)
C5.prerequisite_of.append(C11)
C5.prerequisite_of.append(C12)


db.session.add_all([C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15])
db.session.add_all([L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12])
db.session.add_all([S1,S2,S3,S4,S5,S6,S7,S8])

db.session.commit()