#Student Result Analyzer 

#2.Accepts marks for 5 subjects
subjects = []

print("Enter the 5 subjects names ")
for i in range(5):
    subject = input(f"Enter subject{ i + 1}: ")
    subjects.append(subject)

#get student name 
student_name = input("Enter the name of the Students : ")


subject_marks = {}

for subject in subjects:
       subject_marks[subject] = int(input(f"Enter the {subject} subject Mark : "))

marks = list(subject_marks.values())

# #3.Calculates total
total_mark = 0 
for x in marks :
       total_mark += x 

#4.Calculates average. 
average_mark = total_mark / 5

#5.Determines grade. 

match average_mark:

    case x if average_mark >= 90 :
        grade = "A+"
    case x if average_mark >=80 :
            grade = "A"
    case x if average_mark >=70 :
            grade = "B"
    case x if average_mark >=60 :
            grade = "C"
    case x if average_mark >=50 :
            grade = "D"
    case x if average_mark >= 40 :
            grade = "E"
    case _:
        grade = "F"

#6.Determines Pass/Fail.
if grade != "F" :
       result = "Pass"
else :
       result = "Fail"

#Display result 

print("\n\n")
print("Student Result Analyzer ") 
print(f"Student Name : {student_name}")

for key , value in subject_marks.items() :
       print(f"{key} : {value}")

print()

print(f"Total : {total_mark}")
print(f"Average : {average_mark}")
print(f"Grade : {grade}")
print(f"Result : {result}")

