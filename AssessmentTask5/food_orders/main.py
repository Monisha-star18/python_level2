from src.repositories.food_repository import FoodRepo

foodrepo_object = FoodRepo()
while True :

    print("Menu driven program ")
    print("1.Display all foods ")

    choice = int(input("Enter the users Choice : "))

    match choice :
        case 1 :
            foodrepo_object.display_all_fooditems()
        case _:
            print("Invalid Choice")
