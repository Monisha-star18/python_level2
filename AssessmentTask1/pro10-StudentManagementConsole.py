students = [
    {"name": "Arun", "mark": 85},
    {"name": "Priya", "mark": 92},
    {"name": "Kumar", "mark": 67}
]

is_running = True

while is_running:
    print("\n========== Student Management Console ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Find Topper")
    print("6. Display Passed Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            name = input("Enter student name: ")
            mark = float(input("Enter student mark: "))

            student = { "name": name, "mark": mark}

            students.append(student)
            print("Student added successfully.")

        case 2:
            print("\n---------- Student Details ----------")

            for student in students:
                print(f"Name: {student['name']}")
                print(f"Mark: {student['mark']}")
                print()

        case 3:
            search_name = input("Enter student name to search: ").lower()

            matching_students = [
                student for student in students
                if search_name in student["name"].lower()
            ]

            if matching_students:
                for student in matching_students:
                    print(f"Name: {student['name']}")
                    print(f"Mark: {student['mark']}")
            else:
                print("Student not found.")

        case 4:
            total = sum(student["mark"] for student in students)
            average = total / len(students)

            print(f"Average mark: {average:.2f}")

        case 5:
            marks = [student["mark"] for student in students]

            highest_mark = max(marks)

            print("Highest mark:", highest_mark)


        case 6:
            passed_students = [ student 
                               for student in students 
                               if student["mark"] >= 40 ]

            print("\n---------- Passed Students ----------")

            if passed_students:
                for student in passed_students:
                    print(f"Name: {student['name']}")
            else:
                print("No students passed.")

        case 7:
            print("Thank you.")
            is_running = False

        case _:
            print("Invalid choice.")