#Display All Projects


projects = [
    {"id": 101, "name": "E-Commerce Platform", "company": "TCS", "division": "Web Development", "technology": "Python", "team_size": 8, "budget": 1200000, "status": "Completed", "rating": 4.5},
    {"id": 102, "name": "Banking Application", "company": "TCS", "division": "Backend Development", "technology": "Java", "team_size": 12, "budget": 2500000, "status": "In Progress", "rating": 4.2},
    {"id": 103, "name": "Hospital Management System", "company": "TCS", "division": "Data Science", "technology": "Python", "team_size": 6, "budget": 900000, "status": "Completed", "rating": 4.7},
    {"id": 104, "name": "Food Delivery App", "company": "TCS", "division": "Frontend Development", "technology": "JavaScript", "team_size": 10, "budget": 1800000, "status": "In Progress", "rating": 4.3},
    {"id": 105, "name": "Learning Management System", "company": "TCS", "division": "UI Development", "technology": "React", "team_size": 7, "budget": 1100000, "status": "Completed", "rating": 4.6},
    {"id": 106, "name": "Employee Payroll System", "company": "TCS", "division": "Enterprise Solutions", "technology": "Java", "team_size": 5, "budget": 750000, "status": "Completed", "rating": 4.1},
    {"id": 107, "name": "Travel Booking System", "company": "TCS", "division": "Cloud Development", "technology": "AWS", "team_size": 9, "budget": 1500000, "status": "In Progress", "rating": 4.4},
    {"id": 108, "name": "Inventory Management", "company": "TCS", "division": "Desktop Application", "technology": "C++", "team_size": 4, "budget": 600000, "status": "Completed", "rating": 3.9},
    {"id": 109, "name": "Healthcare Analytics", "company": "TCS", "division": "Machine Learning", "technology": "TensorFlow", "team_size": 11, "budget": 2200000, "status": "In Progress", "rating": 4.8},
    {"id": 110, "name": "Online Banking Portal", "company": "TCS", "division": "Database Development", "technology": "SQL Server", "team_size": 8, "budget": 1700000, "status": "Completed", "rating": 4.0},
    {"id": 111, "name": "Social Media Platform", "company": "TCS", "division": "Full Stack Development", "technology": "Node.js", "team_size": 15, "budget": 3000000, "status": "In Progress", "rating": 4.9},
    {"id": 112, "name": "Customer Support System", "company": "TCS", "division": "Mobile Development", "technology": "Flutter", "team_size": 6, "budget": 950000, "status": "Completed", "rating": 4.5},
    {"id": 113, "name": "Logistics Tracking System", "company": "TCS", "division": "DevOps", "technology": "Docker", "team_size": 14, "budget": 2800000, "status": "In Progress", "rating": 4.7},
    {"id": 114, "name": "Movie Recommendation System", "company": "TCS", "division": "Artificial Intelligence", "technology": "PyTorch", "team_size": 10, "budget": 2100000, "status": "Completed", "rating": 4.8},
    {"id": 115, "name": "CRM Application", "company": "TCS", "division": "API Development", "technology": "REST API", "team_size": 9, "budget": 1600000, "status": "In Progress", "rating": 4.2},
    {"id": 116, "name": "Expense Management App", "company": "TCS", "division": "Cybersecurity", "technology": "Security", "team_size": 5, "budget": 800000, "status": "Completed", "rating": 4.0},
    {"id": 117, "name": "Online Examination System", "company": "TCS", "division": "Testing", "technology": "Selenium", "team_size": 7, "budget": 1000000, "status": "Completed", "rating": 4.4},
    {"id": 118, "name": "AI Chatbot", "company": "TCS", "division": "Generative AI", "technology": "LLM", "team_size": 13, "budget": 3500000, "status": "In Progress", "rating": 4.9},
    {"id": 119, "name": "Document Management System", "company": "TCS", "division": "Cloud Security", "technology": "Azure", "team_size": 8, "budget": 1300000, "status": "Completed", "rating": 3.8},
    {"id": 120, "name": "Cybersecurity Monitoring Tool", "company": "TCS", "division": "Network Engineering", "technology": "Networking", "team_size": 12, "budget": 2700000, "status": "In Progress", "rating": 4.6}
]

def displayProjects():

    for index , project in enumerate(projects,start=1):
        print(f"{index} . {project['name']} - id : {project['id']}")


def searchTechnology(project_tec: str) -> list[dict] :

    project_found = [ project 
                      for project in projects 
                      if project["technology"].lower() == project_tec]

    return project_found

def projectStatistics(project_id:int ) -> tuple[str, str, int, str] | None:

    project_found = [project  for project in projects if  project["id"] == project_id]

    if project_found  :
        return (
                project["technology"],
                project["division"],
                project["team_size"],
                project["status"]
            )
        

    else :
       print("Project Not found!")

def highestBudget() -> dict :

    highestBudget_project = max(projects, key=lambda project : project["budget"])

    return highestBudget_project

def displayProjectsSorted(key : str) -> list[dict] :

    sorted_projects = sorted( projects,  key=lambda project: project[key] )

    return sorted_projects



is_running = True 

while is_running :

    print("""
            ========================================
                PROJECT MANAGEMENT SYSTEM
            ========================================

            1. Display All Projects
            2. Search by Technology
            3. Calculate Statistics
            4. Find Highest Budget Project
            5. Display Projects Sorted by any 
            6. Exit

        """)

    choice = int (input ("Enter your choice (1- 13) : "))

    match choice :

        case 1 :
            displayProjects()

        case 2 :

            project_tec = input("Enter the project Technology to check the project : ").lower()
             
            project_found = searchTechnology(project_tec)

            if project_found :
                for index , project in enumerate(project_found,start=1) :
                    print(f"{index} . {project['name']}")

            else :
                print(f"No project is found in {project_tec} technology")

        case 3 :

            project_id = int (input ("Enter the project ID :  "))

            project_details = projectStatistics(project_id)

            if project_details :

                project_technology , project_division ,  project_team_size , project_status  = project_details

                print(f"{project_id} | {project_technology} | {project_division} | {project_team_size} | {project_status}")

        case 4 :
            
            highestBudget_project = highestBudget()

            print(f"{highestBudget_project['name']} - budget: {highestBudget_project['budget']}")

        case 5 :
            sort_options = { 1: "team_size", 2: "rating", 3: "budget"}

            print("""
                1. Sort by Team Size
                2. Sort by Rating
                3. Sort by Budget
                """)
            
            sort_choice = int(input("Enter your choice: "))

            if sort_choice in sort_options:

                key = sort_options[sort_choice]

                sorted_project = displayProjectsSorted(key)
                
                for project in sorted_project:
                    print(f"{project['name']} - {project[key]}")
    

            else:
                print("Invalid choice!")

            

        case 6 :
            is_running =False

        case _:
            print("invalid choice")

