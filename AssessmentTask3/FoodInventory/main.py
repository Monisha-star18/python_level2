from src.utility.display import display_foods , display_inventory
from src.utility.overwrite_inventory import overwrite_inventory
from src.utility.search import search_foodItem
from src.utility.update_quantity import update_quantity
from src.utility.max_item import maximum_quantity

def display_menu():
        
    print("----------------------------------------")
    print("FOOD INVENTORY SYSTEM")
    print("1. Display Food Items")
    print("2. View Inventory")
    print("3. Overwrite Inventory")
    print("4. Update Quantity")
    print("5. Search Food")
    print("6. Find Food with maximum quantity")
    print("7. Exit")
    print("----------------------------------------")

def main():

    is_running = True 

    while is_running:

        display_menu()

        try:
            choice = int(input("Enter Your choice of opertaion (1-7) : "))

            match choice :
                case 1 :
                    display_foods()

                case 2 :
                    display_inventory()

                case 3 :
                    overwrite_inventory()

                case 4:
                    food_id = int(input("Enter the Food id to be updated :"))
                    
                    update_quantity(food_id)

                case 5:
                    searched_food = input("Enter the food to search : ").lower()
                    search_foodItem(searched_food)

                case 6:
                    maximum_quantity()

                case 7 :
                    print("Thankyou For Your Visti")
                    is_running = False
                    
                case _:
                    print("Invalid Choice")

        except Exception as e  :
            print("----------------------------------------")
            print("Cannot continue due to :  ",e)


if __name__ =='__main__':
    main()


        
