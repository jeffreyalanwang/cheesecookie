from app import db, app
from app import Course, Language, Software, User
from database_wrapper import DBAccess

with app.app_context():
    db.drop_all()
    db.create_all()

    mod = User(id="104780710918021727735", name="Mathew Johnson", email="email@placeholder", picture_url="placeholer",mod_status=True)

    C1 = Course(id=1, title='Introduction to Computer Systems', course_code='ITSC 2181', credit_hours='4', description='Introduction to computer system abstractions reflected in programming languages, operating systems, architectures, and networks. Topics include: overview of computer and processor architecture, instruction set architecture and introduction to assembly language, C programming, system calls, processes and process memory layout, interfaces for memory allocation and file systems, file and directory management via the command line, network architecture and protocols (such as HTTP, MAC, IP, DNS).')
    C2 = Course(id=2, title='Data Structures and Algorithms', course_code='ITSC 2214', credit_hours='3', description='A study of the theory and implementation of abstract data types (ADTs) including stacks, queues, and both general purpose and specialized trees and graphs.  Includes the implementation and analysis of algorithms related to the various data structures studied, including creation, searching, and traversal of ADTs.')
    C3 = Course(id=3, title='Software Engineering', course_code='ITSC 3155', credit_hours='3', description='An introduction to software engineering, which advances the study and application of engineering principles, methods, and techniques that can help us to improve the process of creating software as well as the resulting software products.  The course covers fundamentals of software engineering, including: modern software process models; eliciting, specifying, and evaluating software system requirements; designing software systems to embody required quality attributes, including usability and security; an introduction to reusable software design solutions in the form of software architectural styles and design patterns; software system modeling, implementation, and deployment; and software quality assurance (measurement, inspection, testing).  Project planning, working in teams, and using modern software development tools are also explored.')
    C4 = Course(id=4, title='Introduction to Computer Science I', course_code='ITSC 1212', credit_hours='4', description='Introduction to basic computer literacy, computational thinking and problem-solving using a high level programming language. Programming concepts will be introduced and applied, including: operators; data types; variables, constants, and literals; expressions; control structures and program flow; basic data structures such as arrays, lists, and maps; defining and using functions; file input/output. This is an introductory programming course for non-CS majors and the first course for students interested in pursuing a computer science major or related minor.')
    C5 = Course(id=5, title='Introduction to Computer Science II', course_code='ITSC 1213', credit_hours='4', description='Reinforcement of computational thinking and problem-solving skills. Application of object-oriented programming principles including class design, encapsulation, inheritance, polymorphism, interfaces, abstract classes, aggregation and association. Additional topics include version control, use of debuggers and exception handling. This is the second course for students interested in pursuing a computer science major or related minor.')
    C6 = Course(id=6, title='Computing Professionals', course_code='ITSC 1600', credit_hours='2', description='An introduction to becoming a computing professional. Students learn about setting goals, defining their dream career, becoming a part of the University, planning coursework, building network, managing time, and working in a team.  Additionally, guest speakers and industry panels discuss and explain aspects of a professional career in IT-related fields.  Throughout the course, students build a professional profile including their goals, values, dream career, student organizations, coding skills, communication skills, curriculum plan, professional network, a team TED talk, resume, and a 30-second elevator pitch.')
    C7 = Course(id=7, title='Computer Science Program, Identity, Career', course_code='ITSC 2600', credit_hours='2', description='Introduces the computer science program and develops a student’s identity and career preparedness. Students learn about the program’s progression and graduation requirements, discuss concentration choices, and make curriculum plans. The course stimulates professional identity building emphasizing ethical uses of technology, diversity, career paths, and research.  Course outcomes emphasize an inclusive culture dedicated to student success and equity in the field of computing.')
    C8 = Course(id=8, title='Logic and Algorithms', course_code='ITSC 2175', credit_hours='3', description='A study of discreet mathematical concepts.  Introduction to propositional calculus, predicate calculus, algorithms, logic functions, finite-state machines; and logic design.  ')
    C9 = Course(id=9, title='Introduction to Operating Systems and Networking', course_code='ITSC 3146', credit_hours='3', description='Introduces the fundamentals of operating systems together with the basics of networking and communications.  Topics include: processes, thread, scheduling, cache, memory management, file systems, interprocess communication, network architecture and protocols, HTTP, MAC, IP, TCP/UPD, and Internet routing.  ')
    C10 = Course(id=10, title='Computers and Their Impact on Society', course_code='ITSC 3688', credit_hours='3', description='A study of current topics (software piracy, hacking, professional conduct) in computer science and the impact of computers on various subsets (home, government, and education) of society.')
    C11 = Course(id=11, title='Introduction to Computer Networks', course_code='ITCS 3166', credit_hours='3', description='Internet architecture and protocols. Distributed vs. centralized processing. Data communications; speed; capacity; media, protocols. Network architectures. Evaluation of alternatives. Case studies.')
    C12 = Course(id=12, title='Database Design and Implementation', course_code='ITCS 3160', credit_hours='3', description='Logical and physical database organization, data models, design issues, and secondary storage considerations. Emphasis on actual participation in the design and implementation of databases.')
    C13 = Course(id=13, title='Intro to Video Game Design and Development', course_code='ITCS 4230', credit_hours='3', description='Basic concepts and techniques for electronic game design and development. Topics include: game history and genres, game design teams and processes, what makes a game fun, level and model design, game scripting and programming including computer graphics and animation, artificial intelligence, industry issues, and gender and games.')
    C14 = Course(id=14, title='Web-Based Application Design and Development', course_code='ITIS 3135', credit_hours='3', description='Design and programming concepts for developing interactive web based applications: HTML, CSS, the Document Object Model (DOM), event-driven programming, client side scripting, and web security considerations.')
    C15 = Course(id=15, title='Human-Centered Design', course_code='ITIS 3130', credit_hours='3', description='An introduction to methods and practice of human-centered design for interactive systems.  Topics include: design principles, need finding, design prototypes, and evaluation of interaction designs so that interactive systems are compatible with human capabilities and expectations.  Students learn to work in design teams and write project reports.')
    C16 = Course(id=16, title='Server-Side Applications and Data Management', course_code='ITIS 3105', credit_hours='3', description='This course covers principles that are important for implementing advanced Web-based applications. Emphasis is placed on industrial and business applications which require robust and secure implementations. Server-side scripting and processing techniques are exercised in course projects.')

    L1 = Language(id=1, name='Python', site_url='https://www.python.org/', download_url='https://www.python.org/downloads/', documentation_url='https://docs.python.org/', description='Python is an interpreted, object-oriented, and high-level programming language with dynamic semantics. Its high-level built-in data structures, combined with dynamic typing and dynamic binding, make it useful for rapid development. Python is also commonly used as a scripting or glue language to connect existing components together.')
    L2 = Language(id=2, name='C', download_url='https://gcc.gnu.org/', documentation_url='https://www.gnu.org/software/gnu-c-manual/', description='A general-purpose, procedural, and high-level programming language developed in the 1970s. It is designed to be compiled to provide low-level access to memory and language constructs that map efficiently to machine instructions. Widely used in the development of various applications and operating systems. It is considered the base for other programming languages, and knowledge of C can make it easier to learn other languages.')
    L3 = Language(id=3, name='RISC-V', site_url='https://riscv.org', documentation_url='https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf', description='RISC-V is an open standard Instruction Set Architecture (ISA) enabling a new era of processor innovation through open collaboration')
    L4 = Language(id=4, name='SQL', documentation_url='https://dev.mysql.com/doc/', description='Used to manage data, especially in a relational database management system. Can handle data incorporating relations among entities and variables. SQL allows programmers to query a database for information, manipulate data (insert, update, and delete), define data (schema creation and modification), and control data access.')
    L5 = Language(id=5, name='HTML', site_url='https://www.w3.org/html/', documentation_url='https://developer.mozilla.org/en-US/docs/Web/HTML', description='Used to create and structure webpage content. It organizes documents and defining elements on them, creating relationships between them. HTML is not a programming language, but it is an important language in web development.')
    L6 = Language(id=6, name='CSS', site_url='https://www.w3.org/Style/CSS/', documentation_url='https://developer.mozilla.org/en-US/docs/Web/css', description='Used for specifying the styling of an HTML document. Allows control of layout, color, and font, and can adapt to different-sized screens. CSS is not a programming language itself, but instead is used to add styling.')
    L7 = Language(id=7, name='JavaScript', documentation_url='https://developer.mozilla.org/en-US/docs/Web/JavaScript', description='JavaScript is a lightweight interpreted programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript is a prototype-based, multi-paradigm, single-threaded, dynamic language, supporting object-oriented, imperative, and declarative styles.')
    L8 = Language(id=8, name='Java', site_url='https://www.java.com/en/', download_url='https://www.java.com/en/download/', documentation_url='https://docs.oracle.com/en/java/', description='Java is a programming language and computing platform first released by Sun Microsystems in 1995. It has evolved from humble beginnings to power a large share of today’s digital world, by providing the reliable platform upon which many services and applications are built. New, innovative products and digital services designed for the future continue to rely on Java, as well.')
    L9 = Language(id=9, name='C++', site_url='https://isocpp.org/', documentation_url='https://devdocs.io/cpp/', description='A high-level, general-purpose programming language created as an extension of the C language. A cross-platform language that can be used to create high-performance applications, with a high level of control over system resources and memory. Object-oriented features provide clear structure and simplify code reuse.')
    L10 = Language(id=10, name='GML', site_url='https://manual.gamemaker.io/monthly/en/GameMaker_Language/GameMaker_Language_Index.htm', download_url='https://gamemaker.io/en/download', documentation_url='https://manual.gamemaker.io/monthly/en/GameMaker_Language/GameMaker_Language_Index.htm', description='GML is a programming language used in Game Maker Studio. It takes elements from Java, Python, and C#.')
    L11 = Language(id=11, name='C#', documentation_url='https://learn.microsoft.com/en-us/dotnet/csharp/', description='C# is a cross-platform general purpose language that makes developers productive while writing highly performant code. With millions of developers, C# is the most popular .NET language.')
    L12 = Language(id=12, name='Bash', site_url='https://www.gnu.org/software/bash/', documentation_url='https://www.gnu.org/software/bash/manual/', description='Unix shell and scripting language. A popular command line interpreter that provides a powerful environment for command execution, task automation, and the creation of complex scripts.')

    S1 = Software(id=1, name='VS Code', site_url='https://code.visualstudio.com/', download_url='https://code.visualstudio.com/Download', documentation_url='https://code.visualstudio.com/docs', description='A free, open-source, and lightweight code editor developed by Microsoft, optimized for building and debugging modern web and cloud applications, and supports multiple programming languages and platforms.')
    S2 = Software(id=2, name='Wireshark', site_url='https://www.wireshark.org/', download_url='https://www.wireshark.org/download.html', documentation_url='https://www.wireshark.org/docs/', description='A popular open-source network protocol analyzer that captures and displays packets from a network connection in detail.')
    S3 = Software(id=3, name='Oracle VirtualBox', site_url='https://www.virtualbox.org/', download_url='https://www.virtualbox.org/wiki/Downloads', documentation_url='https://www.virtualbox.org/wiki/Documentation', description='Open-source, cross-platform virtualization software that allows users to run multiple operating systems on a single device. Popular for developing, testing, and network administration.')
    S4 = Software(id=4, name='Ubuntu', site_url='https://ubuntu.com/', download_url='https://ubuntu.com/download', documentation_url='https://help.ubuntu.com/', description='A free, open-source, and user-friendly Linux distribution based on Debian, developed by the British company Canonical, offering multiple editions for desktop, server, and IoT devices.')
    S5 = Software(id=5, name='Imunes', site_url='https://imunes.net/', download_url='https://imunes.net/download', documentation_url='https://imunes.net/dl/guide/', description='IMUNES (Integrated Multiprotocol Network Emulator/Simulator) is a fast, functional network simulator. It simulates IP networks by creating virtual nodes on a FreeBSD host system, using the FreeBSD Jails virtualization feature. This allows for the creation of networks of interconnected virtual machines that can emulate network elements, making it a powerful tool for network analysis and testing.')
    S6 = Software(id=6, name='Game Maker Studio 2', site_url='https://gamemaker.io/en', download_url='https://gamemaker.io/en/download', documentation_url='https://gamemaker.io/en/tutorials', description='A game engine that is is primarily focused on the development of 2D Games')
    S7 = Software(id=7, name='MySQL Workbench', site_url='https://www.mysql.com/products/workbench/', download_url='https://dev.mysql.com/downloads/workbench/', documentation_url='https://dev.mysql.com/doc/workbench/en/', description='MySQL Workbench is a unified visual tool for database architects, developers, and DBAs. MySQL Workbench provides data modeling, SQL development, and comprehensive administration tools for server configuration, user administration, backup, and much more. MySQL Workbench is available on Windows, Linux and Mac OS X.')
    S8 = Software(id=8, name='Unity', site_url='https://unity.com/', download_url='https://unity.com/pricing', documentation_url='https://docs.unity.com/', description='Unity’s real-time 3D development engine lets artists, designers, and developers collaborate to create amazing immersive and interactive experiences. You can work on Windows, Mac, and Linux.')
    S9 = Software(id=9, name='NetBeans', site_url='https://netbeans.apache.org/front/main/index.html', download_url='https://netbeans.apache.org/front/main/download/', documentation_url='https://netbeans.apache.org/tutorial/main/kb/', description='NetBeans is an IDE primarily used for Java development. It allows applications to be developed from a set of modular software components called modules.')


    C1.course_requires.append(C4)
    C2.course_requires.append(C5)
    C3.course_requires.append(C2)
    C5.course_requires.append(C4)
    C8.course_requires.append(C4)
    C9.course_requires.append(C1)
    C9.course_requires.append(C2)
    C11.course_requires.append(C5)
    C12.course_requires.append(C5)
    C13.course_requires.append(C2)
    C14.course_requires.append(C2)
    C15.course_requires.append(C2)
    C16.course_requires.append(C5)
    C16.course_requires.append(C14)

    C1.compatible_language.append(L2)
    C1.compatible_language.append(L3)
    C2.compatible_language.append(L8)
    C3.compatible_language.append(L1)
    C3.compatible_language.append(L4)
    C3.compatible_language.append(L5)
    C3.compatible_language.append(L6)
    C4.compatible_language.append(L1)
    C5.compatible_language.append(L8)
    C6.compatible_language.append(L1)
    C9.compatible_language.append(L9)
    C12.compatible_language.append(L4)
    C13.compatible_language.append(L9)
    C14.compatible_language.append(L5)
    C14.compatible_language.append(L6)
    C14.compatible_language.append(L7)
    C16.compatible_language.append(L1)
    C16.compatible_language.append(L12)

    S1.compatible_course.append(C1)
    S1.compatible_course.append(C3)
    S1.compatible_course.append(C14)
    S2.compatible_course.append(C9)
    S2.compatible_course.append(C11)
    S3.compatible_course.append(C9)
    S3.compatible_course.append(C1)
    S4.compatible_course.append(C9)
    S4.compatible_course.append(C1)
    S4.compatible_course.append(C16)
    S5.compatible_course.append(C9)
    S6.compatible_course.append(C13)
    S7.compatible_course.append(C12)
    S9.compatible_course.append(C2)

    L1.compatible_software.append(S1)
    L2.compatible_software.append(S1)
    L2.compatible_software.append(S9)
    L4.compatible_software.append(S7)
    L5.compatible_software.append(S1)
    L5.compatible_software.append(S9)
    L6.compatible_software.append(S1)
    L7.compatible_software.append(S1)
    L7.compatible_software.append(S9)
    L8.compatible_software.append(S9)
    L9.compatible_software.append(S1)
    L9.compatible_software.append(S9)
    L10.compatible_software.append(S6)
    L11.compatible_software.append(S1)
    L11.compatible_software.append(S9)
    L12.compatible_software.append(S4)


    db.session.add(mod)
    db.session.add_all([C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16])
    db.session.add_all([L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12])
    db.session.add_all([S1,S2,S3,S4,S5,S6,S7,S8,S9])

    db.session.commit()
