import csv 
from ..config import get_inventoryPath 
from .read_file import read_file


def update_quantity(food_id:int ) ->None:

    food_quantites = read_file(get_inventoryPath())

    if not food_quantites :
        print("There is not food items")
        return

    is_found = False

    for food_item in food_quantites :
        if int(food_item['food_id']) == food_id :
            is_found = True
            break
    
    if is_found :
        while True :
            try:
                update_quantity = int (input("Enter the quantity to update : "))
        
                if update_quantity >= 0 :
                    food_item['quantity'] = update_quantity
                    write(food_quantites)
                    break
                else:
                    print("Quantity cannot be negative")
                    
            except ValueError:
                print("Enter only interger value for quantity ")

    else:
        print("The food id not found ")

def write(food_quantites):
    with open(get_inventoryPath(),"w",newline="") as inventory_file:
        inventory_writer =csv.DictWriter(inventory_file,fieldnames=["food_id","quantity"])
        inventory_writer.writeheader()
        inventory_writer.writerows(food_quantites)


       


    
