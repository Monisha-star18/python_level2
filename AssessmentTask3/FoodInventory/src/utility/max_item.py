from ..config import get_inventoryPath, get_foodPath
from .read_file import read_file


def maximum_quantity() -> None:

    inventory = read_file(get_inventoryPath())

    if not inventory:
        print("No inventory found.")
        return

    max_item = max( inventory, key=lambda item: int(item["quantity"]))

    print("Food with maximum quantity:")
    print(f"Food ID  : {max_item['food_id']}")
    print(f"Quantity : {max_item['quantity']}")