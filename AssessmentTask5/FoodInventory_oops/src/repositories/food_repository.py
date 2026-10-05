from pathlib import Path

from src.models.food import Food
from src.utility.read_file import read_file
from src.utility.write_file import write_file


class FoodRepository:

    def __init__(self, file_path: Path) -> None:

        self.file_path = file_path

    # Read all foods from CSV
    def get_all(self) -> list[Food]:

        rows = read_file(self.file_path)

        foods = []

        for row in rows:

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

            foods.append(food)

        return foods

    # Save all foods to CSV
    def save_all(self, foods: list[Food]) -> None:

        rows = []

        for food in foods:
            
            rows.append({ "food_id": str(food.food_id),
                "food_name": food.food_name,
                "category": food.category,
                "price": str(food.price),
                "cost_price": str(food.cost_price),
                "stock_quantity": str(food.stock_quantity),
                "tax_percent": str(food.tax_percent),
                "discount_percent": str(food.discount_percent),
                "rating": str(food.rating)
            })

        write_file(
            self.file_path,
            rows,[
                "food_id",
                "food_name",
                "category",
                "price",
                "cost_price",
                "stock_quantity",
                "tax_percent",
                "discount_percent",
                "rating"
            ]
        )