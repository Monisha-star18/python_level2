from src.models.food import Food
from src.models.order import Order
from src.utility.display import money, print_details, print_table


class OrderService:

    def __init__(self, orders: list[Order], foods: list[Food]) -> None:

        self.orders = orders
        self.foods = foods

    def _food_name(self, food_id: int) -> str:

        for food in self.foods:
            if food.food_id == food_id:
                return food.food_name

        return "Unknown"

    # Display all orders as a table
    def display_orders(self) -> None:

        if not self.orders:
            print("No orders found.")
            return

        self.display_order_table(self.orders)

    # Print a list of orders as a table
    def display_order_table(self, orders: list[Order]) -> None:

        print_table(
            ["Order ID", "Customer", "Food", "Qty", "Date", "Status", "Payment", "Total"],
            [ [  o.order_id, o.customer_name, self._food_name(o.food_id), o.quantity, o.order_date.isoformat(), o.status, o.payment_method, money(self.calculate_order_total(o)),] for o in orders ],
        )

    # Print a single order neatly
    def display_order_details(self, order: Order) -> None:

        print_details(
            f"ORDER #{order.order_id}",
            [
                ("Customer", order.customer_name),
                ("Food", f"{self._food_name(order.food_id)} (ID {order.food_id})"),
                ("Quantity", str(order.quantity)),
                ("Date", order.order_date.isoformat()),
                ("Status", order.status),
                ("Payment", order.payment_method),
                ("Total", money(self.calculate_order_total(order))),
            ],
        )

    # Find order by order ID
    def find_order_by_id(self, order_id: int) -> Order | None:

        for order in self.orders:
            if order.order_id == order_id:
                return order

        return None

    # Find orders by status
    def find_orders_by_status(self, status: str) -> list[Order]:

        return [
            order
            for order in self.orders
            if order.status.lower() == status.lower()
        ]

    # Calculate total of one order
    def calculate_order_total(self, order: Order) -> float:

        for food in self.foods:
            if food.food_id == order.food_id:
                return food.price * order.quantity

        return 0.0

    # Calculate total revenue (completed orders only)
    def calculate_total_revenue(self) -> float:

        total = 0.0

        for order in self.orders:
            if order.status.lower() == "completed":
                total += self.calculate_order_total(order)

        return total

    # Calculate number of orders
    def calculate_total_orders(self) -> int:
        return len(self.orders)
