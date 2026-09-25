import csv
from pathlib import Path

def read_file(path_received):

    path = Path(path_received)

    if path.is_file() :
            with open(path,"r") as file :
                
                reader = csv.DictReader(file)

                return list(reader)
    else:
            print("File not found")
            return []

