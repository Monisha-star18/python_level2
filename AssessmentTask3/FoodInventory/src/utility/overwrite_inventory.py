import csv 
from ..config import get_inventoryPath , get_foodPath
from .read_file import read_file

inventory_fieldnames = ["food_id","quantity"]

def overwrite_inventory():

    food_items = read_file(get_foodPath())

    if not food_items :
        print("There is not food items")
        return 

    with open(get_inventoryPath(),"w",newline="") as inventory_file:
        
        inventory_writer =csv.DictWriter(inventory_file , fieldnames= inventory_fieldnames)
        inventory_writer.writeheader()

        for food in food_items :

            while True :
                try:
                    quantity = int(input(f"Enter the quanity for {food['food_id']}-{food['food_name']} : "))
                    
                    if quantity >= 0 :
                        inventory_item = { "food_id": food["food_id"], "quantity": quantity }
                        inventory_writer.writerow(inventory_item)
                        break

                    else :
                        print("Quantity cannot be negative")
                        
                except ValueError :
                    print("Enter only interger value for quantity ")
                
        print("Inventory overwritten successfully.")

        

        