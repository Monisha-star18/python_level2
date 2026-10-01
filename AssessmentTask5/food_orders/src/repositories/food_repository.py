from src.services.food_service import FoodServices
from src.exception.exception import DataNotFoundError

foodservices_object = FoodServices()

class FoodRepo :

    def __init__(self):
        pass

    def display_all_fooditems(self) :
        food_items = foodservices_object.get_food_item()

        try :
            if not food_items :
                raise DataNotFoundError()
            else:
                print(food_items)
        except DataNotFoundError as error :
            print(error)

        
