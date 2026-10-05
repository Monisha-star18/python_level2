from pathlib import Path
from datetime import date

from src.models.order import Order
from src.utility.read_file import read_file
from src.utility.write_file import write_file


class OrderRepository:

    def __init__(self, file_path: Path) -> None:

        self.file_path = file_path

    # Read all orders from CSV
    def get_all(self) -> list[Order]:

        rows = read_file(self.file_path)

        orders = []

        for row in rows:

            order = Order( order_id=int(row["order_id"]),
                            customer_name=row["customer_name"],
                            food_id=int(row["food_id"]),
                            quantity=int(row["quantity"]),
                            order_date=date.fromisoformat(row["order_date"]),
                            status=row["status"],
                            payment_method=row["payment_method"] )

            orders.append(order)

        return orders

    # Add a new order
    def add(self, order: Order) -> None:

        orders = self.get_all()
        orders.append(order)
        self.save_all(orders)

    # Save all orders to CSV
    def save_all( self, orders: list[Order] ) -> None:

        rows = []

        for order in orders:

            rows.append({   "order_id": str(order.order_id),
                            "customer_name": order.customer_name,
                            "food_id": str(order.food_id),
                            "quantity": str(order.quantity),
                            "order_date": order.order_date.isoformat(),
                            "status": order.status,
                            "payment_method": order.payment_method
                        })

        write_file( self.file_path,
            rows, [ "order_id", "customer_name", "food_id", "quantity", "order_date", "status", "payment_method"]
        )