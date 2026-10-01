from config import get_foods_data_path 
from src.utitity.read import read_data


class FoodServices :

    def __init__(self):
        self.food_path = get_foods_data_path()

    def get_food_item(self):
        data = read_data(self.food_path)
        return data