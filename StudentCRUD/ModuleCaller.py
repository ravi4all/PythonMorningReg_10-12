#import StudentModule
from com import StudentModule

mainLoop = True

while mainLoop:

    print("""
******** Main Menu ********
1. Add Student
2. Delete Student
3. Read Students
4. Update Student
5. Save Student
6. Load Student
q. Quit
""")

    choice = input("Enter your choice : ")

    todo = {
        "1" : StudentModule.addStudent,
        "2" : StudentModule.deleteStudent,
        "3" : StudentModule.readStudent,
        "4" : StudentModule.updateStudent,
        "5" : StudentModule.saveStudent,
        "6" : StudentModule.loadStudent,
        "q" : quit}

    todo.get(choice, StudentModule.errHandler)()
