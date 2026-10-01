import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def get_foods_data_path():
    return Path(os.getenv('FOODS_PATH'))

def get_orders_data_path():
    return Path(os.getenv('ORDERS_PATH'))
