
employees = {
    101: {"Name": "Monisha", "Age": 20, "Salary": 20000, "Department": "IT"},
    102: {"Name": "Sanjay", "Age": 24, "Salary": 28000, "Department": "HR"},
    103: {"Name": "Vishal", "Age": 23, "Salary": 32000, "Department": "Finance"},
    104: {"Name": "Priya", "Age": 25, "Salary": 35000, "Department": "Marketing"},
    105: {"Name": "Arun", "Age": 27, "Salary": 40000, "Department": "IT"},
    106: {"Name": "Divya", "Age": 22, "Salary": 26000, "Department": "Sales"},
    107: {"Name": "Karthik", "Age": 29, "Salary": 45000, "Department": "Finance"},
    108: {"Name": "Keerthana", "Age": 26, "Salary": 38000, "Department": "HR"},
    109: {"Name": "Rahul", "Age": 30, "Salary": 50000, "Department": "IT"},
    110: {"Name": "Swetha", "Age": 24, "Salary": 30000, "Department": "Marketing"}
}
is_running = True

while is_running:

    print("\n========== Employee Management Console ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Find Highest Salary")
    print("5. Display Employees by Department")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\n---------- Add Employee ----------")

            employee_id = int(input("Enter Employee ID: "))

            if employee_id in employees:
                print("Employee ID already exists.")
            else:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                salary = float(input("Enter Salary: "))
                department = input("Enter Department: ")

                employee = {  "employee_name": name,  "Age": age,  "Salary": salary, "Department": department}

                employees[employee_id] = employee

                print("Employee added successfully.")

        case 2:
            print("\n---------- Employee Details ----------")

            for employee_id, employee_details in employees.items():
                print(f"\nEmployee ID: {employee_id}")
                print(f"Name: {employee_details['Name']}")
                print(f"Age: {employee_details['Age']}")
                print(f"Salary: ₹{employee_details['Salary']}")
                print(f"Department: {employee_details['Department']}")

        case 3:
            print("\n---------- Search Employee ----------")

            search_name = input("Enter employee name to search: ").lower()

            matching_employees = [
                (employee_id, employee)
                for employee_id, employee in employees.items()
                if search_name in employee["Name"].lower()
            ]

            if matching_employees:
                for employee_id, employee in matching_employees:
                    print(f"\nEmployee ID: {employee_id}")
                    print(f"Name: {employee['Name']}")
                    print(f"Age: {employee['Age']}")
                    print(f"Salary: ₹{employee['Salary']}")
                    print(f"Department: {employee['Department']}")
            else:
                print("Employee not found.")

        case 4:
            print("\n---------- Highest Salary ----------")

            highest_salary = max( employee["Salary"] for employee in employees.values() )

            highest_paid_employees = [
                (employee_id, employee)
                for employee_id, employee in employees.items()
                if employee["Salary"] == highest_salary
            ]

            for employee_id, employee in highest_paid_employees:
                print(f"Employee ID: {employee_id}")
                print(f"Name: {employee['Name']}")
                print(f"Salary: ₹{employee['Salary']}")
                print(f"Department: {employee['Department']}")

        case 5:
            print("\n---------- Employees by Department ----------")

            department = input("Enter Department: ").lower()

            department_employees = [
                (employee_id, employee)
                for employee_id, employee in employees.items()
                if employee["Department"].lower() == department
            ]

            if department_employees:
                print(f"\nEmployees in {department.title()} Department:")

                for employee_id, employee in department_employees:
                    print(f"\nEmployee ID: {employee_id}")
                    print(f"Name: {employee['Name']}")
                    print(f"Age: {employee['Age']}")
                    print(f"Salary: ₹{employee['Salary']}")
            else:
                print("No employees found in this department.")

        case 6:
            print("\nThank you for using Employee Management Console.")
            is_running = False

        case _:
            print("Invalid choice. Please select a number from 1 to 6.")
