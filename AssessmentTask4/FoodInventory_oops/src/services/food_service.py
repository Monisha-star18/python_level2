from src.models.food import Food
from src.utility.display import money, print_details, print_table


class FoodService:

    def __init__(self, foods: list[Food]) -> None:
        self.foods = foods

    # Display all foods as a table
    def display_foods(self) -> None:

        if not self.foods:
            print("No food items found.")
            return

        print_table(
            ["ID", "Name", "Category", "Price", "Stock"],
            [ [f.food_id, f.food_name, f.category, money(f.price), f.stock_quantity]  for f in self.foods ],
        )

    # Search food by name (case-insensitive, partial match allowed)
    def search_food(self, name: str) -> list[Food]:

        name = name.lower()
        return [food for food in self.foods if name in food.food_name.lower()]

    # Show search results neatly
    def display_search_results(self, results: list[Food]) -> None:

        if not results:
            print("Food not found.")
            return

        if len(results) == 1:
            food = results[0]
            print_details(
                f"FOOD #{food.food_id}",
                [
                    ("Name", food.food_name),
                    ("Category", food.category),
                    ("Price", money(food.price)),
                    ("Stock", str(food.stock_quantity)),
                    ("Discount", f"{food.discount_percent:g}%"),
                    ("Tax", f"{food.tax_percent:g}%"),
                    ("Rating", f"{food.rating:.1f} / 5"),
                ],
            )
            return

        print_table(
            ["ID", "Name", "Category", "Price", "Stock", "Rating"],
            [ [f.food_id, f.food_name, f.category, money(f.price),  f.stock_quantity, f"{f.rating:.1f}"] for f in results ],
        )

    # Find the food with the maximum price
    def find_maximum_price(self) -> Food | None:

        if not self.foods:
            return None

        return max(self.foods, key=lambda food: food.price)

    # Find the food with the minimum price
    def find_minimum_price(self) -> Food | None:

        if not self.foods:
            return None

        return min(self.foods, key=lambda food: food.price)

    # Find a food by ID
    def find_food_by_id(self, food_id: int) -> Food | None:

        for food in self.foods:
            if food.food_id == food_id:
                return food

        return None
