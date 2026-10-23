"""Repository that loads and saves ``Food`` records from a CSV file."""

from pathlib import Path
from src.exceptions.exceptions import DataLoadError
from src.models.food import Food
from src.utility.read_file import read_file
from src.utility.write_file import write_file

# CSV columns for foods  (used for reading and writing).
FOOD_FIELDNAMES: list[str] = [
    "food_id",
    "food_name",
    "category",
    "price",
    "cost_price",
    "stock_quantity",
    "tax_percent",
    "discount_percent",
    "rating",
]

"""Reads and writes foods to a CSV file."""
class FoodRepository:

    def __init__(self, file_path: Path) -> None:
        """Store the CSV location."""
        self.file_path:Path  = file_path

    #Read all foods deatils  from CSV.
    def get_all(self) -> list[Food]:

        try:
            rows:list[dict[str, str]] = read_file(self.file_path)

        except FileNotFoundError as exc:
            raise DataLoadError(
                f"Food file not found: {self.file_path}"
                ) from exc

        foods:list[Food]

        for line_number ,row in enumerate(rows,start=2):
            try:

                food = Food(
                    food_id=int(row["food_id"]),
                    food_name=row["food_name"],
                    category=row["category"],
                    price=float(row["price"]),
                    cost_price=float(row["cost_price"]),
                    stock_quantity=int(row["stock_quantity"]),
                    tax_percent=float(row["tax_percent"]),
                    discount_percent=float(row["discount_percent"]),
                    rating=float(row["rating"])
                )

            except KeyError as exc:
                raise DataLoadError(
                    f"{self.file_path.name} line {line_number}: missing column {exc}"
                ) from exc
            
            except ValueError as exc:
                raise DataLoadError(
                    f"{self.file_path.name} line {line_number}: invalid value ({exc})"
                ) from exc

            foods.append(food)

        return foods

    # Overwrite the CSV file with the given foods 
    def save_all(self, foods: list[Food]) -> None:

        rows : list[dict[str,str]]= [
            { 
                "food_id": str(food.food_id),
                "food_name": food.food_name,
                "category": food.category,
                "price": str(food.price),
                "cost_price": str(food.cost_price),
                "stock_quantity": str(food.stock_quantity),
                "tax_percent": str(food.tax_percent),
                "discount_percent": str(food.discount_percent),
                "rating": str(food.rating)
            }
            for food in foods  
        ]

        write_file( self.file_path, rows,FOOD_FIELDNAMES)