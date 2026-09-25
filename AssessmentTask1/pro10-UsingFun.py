"""
10. Student Management Console ⭐⭐⭐
Menu:
1. Add Student
2. View Students
3. Search Student
4. Calculate Average
5. Find Topper
6. Display Passed Students
7. Exit
Use a list of dictionaries.

"""
students = [
    {"name": "Arun", "mark": 85},
    {"name": "Priya", "mark": 92},
    {"name": "Kumar", "mark": 67}
]

def hasStudents():
    return bool(students)

def addStudent(student_name,student_mark):

    student = { "name" : student_name , "mark" : student_mark }

    students.append(student)

    print(f"The student {student_name} is been added to the database ")


def viewStudents():

    if hasStudents():
         for student in students :
             print(f" Student name : {student["name"]} | Mark : {student["mark"]} ")
    else :
        print("The student databse is empty")
        
def searchStudent(student_name):

    if hasStudents():

        student_found = [ student 
                         for student in students 
                         if student_name in student["name"].lower()]

        return student_found

    else:
        print("The student databse is empty")
    

def calculateAverage():

    if hasStudents():
        total_marks = sum(student["mark"] for student in students )

        average_marks = total_marks / len(students)

        return average_marks
    
    else:
        print("The student databse is empty")

    
         
def findTopper():

    if hasStudents():
        top_student = max(students , key=lambda student : student["mark"])
        
        return top_student
    else:
        print("The student databse is empty")


def displayPassedStudents():

    if hasStudents():

        passed_students = [ student 
                            for student in students 
                            if student["mark"] >= 40 ]

        return passed_students
    else:
            print("The student databse is empty")
    


is_running = True

while is_running:

    print("***************************************************")
    print("Welcome to the Student Management Console")
    print("""
            Menu:
                1. Add Student
                2. View Students
                3. Search Student
                4. Calculate Average
                5. Find Topper
                6. Display Passed Students
                7. Exit
            """)

    choice = int(input ("Enter the operation you would like to perform (1-7) :"))

    match choice :
        #Add Student
        case 1:

            student_name = input("Enter student name : ")
            student_mark = float(input("Enter the students mark "))
            
            addStudent(student_name,student_mark)

        #View Students
        case 2 :
            viewStudents()

        #Search Student
        case 3 :

            student_name = input("Enter student name : ").lower()

            student_found = searchStudent(student_name)

            if student_found :
                        for student in student_found:
                            print("Student found ! ")
                            print(f" Student name : {student["name"]} | Mark : {student["mark"]} ")

            else :
                print("Student not found ! ")

        #Calculate Average
        case 4 :
            average_marks = calculateAverage()
            print(f"Calculated Average mark is : {average_marks} ")

        #Find Topper
        case 5 :
            top_student = findTopper()
            print(f"Topper: {top_student['name']} with {top_student['mark']} marks")

        #Display Passed Students
        case 6 :
            passed_students = displayPassedStudents()

            if passed_students:
                for student in passed_students:
                    print(f"Name: {student['name']}")

            else:
                print("No students passed.")

        case 7 :
            print("Thank You for your visit ")
            is_running =False

        case _ :
            print("Invalid choice.")
            





