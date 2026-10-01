import json
from pathlib import Path

from src.exception.exception import FileNotFound

def read_data(file_path:Path ):

    if not file_path.is_file() : 
        raise FileNotFound

    with file_path.open('r') as file :

        json_read = json.load(file)

    return json_read
