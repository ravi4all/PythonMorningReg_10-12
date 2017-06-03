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
    try:
        del(studentList[toDelete-1])
        print("Updated Student List")
        for s in studentList:
            print(s)

    except:
        print("Student do not exist")


def readStudent():
    for s in studentList:
        print(s)

def updateStudent():
    pass

def saveStudent():
    file = open("StudentList.txt",'a+')
    for student in studentList:
        s = str(student).strip("[]")
        file.write(s+"\n")
    print("Written Data Successfully")
    file.close()

def loadStudent():
    file = open("StudentList.txt",'r')
    a = file.read()
    print("Data Loaded")
    print(a)

def errHandler():
    print("Wrong choice, Press Again")
