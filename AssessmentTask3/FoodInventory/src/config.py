from dotenv import load_dotenv
from pathlib import Path
import os 

load_dotenv()

def get_foodPath() -> Path:
    return Path(os.getenv("FOOD_PATH"))

def get_inventoryPath()->Path:
    return Path(os.getenv("INVENTORY_PATH"))