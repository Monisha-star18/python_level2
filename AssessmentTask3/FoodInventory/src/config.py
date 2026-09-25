from dotenv import load_dotenv
from pathlib import Path
import os 

load_dotenv()

def get_foodPath():
    return Path(os.getenv("FOOD_PATH"))

def get_inventoryPath():
    return Path(os.getenv("INVENTORY_PATH"))