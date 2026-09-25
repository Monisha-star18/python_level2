from ..config import get_foodPath
from .read_file import read_file

def search_foodItem (searched_food):

    food_items = read_file(get_foodPath())

    if not food_items :
        print("There is not food items")
        return

    is_Found = False

    for food_item in food_items :
        if food_item['food_name'].lower() == searched_food :
            is_Found = True
        
    if is_Found :
        print("The Food item exists")
        
        print(f" ID : {food_item['food_id']}   |"
            f"  Name : {food_item['food_name']}  |"
            f"  Quantity Left : {food_item['category']}     |"
            f" Price : $ {food_item['price']}"
            )
        
    else:
        print("The Food item dont exists")
