studentList = []

def addStudent():
    id = 0
    #id = int(input("Enter student id : "))
    name = input("Enter name of student : ")
    cgpa = input("Enter CGPA of student : ")

    studentList.append([name,cgpa])

    for s in studentList:
        id += 1
        print(id,s)

def deleteStudent():
    toDelete = int(input("Enter student ID to delete : "))

    #index_of_toDelete = studentList.index(toDelete-1)
    
    del(studentList[toDelete-1])

    print("Updated Student List")
    for s in studentList:
        print(s)


def readStudent():
    for s in studentList:
        print(s)

def updateStudent():
    pass

def errHandler():
    print("Wrong choice, Press Again")


mainLoop = True

while mainLoop:

    print("""
******** Main Menu ********
1. Add Student
2. Delete Student
3. Read Students
4. Update Student
5. Quit
""")

    choice = input("Enter your choice : ")

    todo = {
        "1" : addStudent,
        "2" : deleteStudent,
        "3" : readStudent,
        "4" : updateStudent,
        "5" : quit}

    todo.get(choice, errHandler)()
