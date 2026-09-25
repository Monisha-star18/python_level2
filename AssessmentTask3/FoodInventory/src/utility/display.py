from ..config import get_foodPath , get_inventoryPath
from .read_file import read_file


#display the main Food 
def display_foods ():
    try:
        reader = read_file(get_foodPath())
        
        if reader:
            for food_item in reader :
                print(f" ID : {food_item['food_id']}   |"
                    f"  Name : {food_item['food_name']}  |"
                    f"  Quantity Left : {food_item['category']}      |"
                    f" Price : $ {food_item['price']}"
                    )
        else :
            print("No food items found.")
            
    except Exception as e :
        print("The error in the display foods " , e)

#display the Inventory 
def display_inventory():

    try:
        reader = read_file(get_inventoryPath())

        if reader:
            for iv_data in reader :
                print(f" ID : {iv_data['food_id']}   |"
                    f" Quantity  : {iv_data['quantity']} ")
        else :
            print("No inventory detils found items found.")
            
    except Exception as e :
            print("The error in the display inventory " , e)
