"""Repository that loads and saves ``Order`` records from a CSV file."""

from pathlib import Path
from datetime import date

from src.exceptions.exceptions import DataLoadError
from src.models.order import Order
from src.utility.read_file import read_file
from src.utility.write_file import write_file

# CSV columns for orders  (used for reading and writing).
ORDER_FIELDNAMES: list[str] = [
    "order_id",
    "customer_name",
    "food_id",
    "quantity",
    "order_date",
    "status",
    "payment_method",
]
 
"""Reads and writes orders to a CSV file."""
class OrderRepository:

    def __init__(self, file_path: Path) -> None:
        """Store the CSV location."""
        self.file_path:Path  = file_path

    # Read all orders from CSV
    def get_all(self) -> list[Order]:

        try:
            rows:list[dict[str,str]] = read_file(self.file_path)

        except FileNotFoundError as exc:
            raise DataLoadError(f"Order  file not found: {self.file_path}") from exc


        orders:list[Order] = [
            Order( 
                    order_id=int(row["order_id"]),
                    customer_name=row["customer_name"],
                    food_id=int(row["food_id"]),
                    quantity=int(row["quantity"]),
                    order_date=date.fromisoformat(row["order_date"]),
                    status=row["status"],
                    payment_method=row["payment_method"]
                )
            for row in rows
        ]

        return orders

    # Add a new order
    def add(self, order: Order) -> None:

        orders = self.get_all()
        orders.append(order)
        self.save_all(orders)

    # Save all orders to CSV
    def save_all( self, orders: list[Order] ) -> None:

        rows:list[dict[str,str]] = [
            {   
                "order_id": str(order.order_id),
                "customer_name": order.customer_name,
                "food_id": str(order.food_id),
                "quantity": str(order.quantity),
                "order_date": order.order_date.isoformat(),
                "status": order.status,
                "payment_method": order.payment_method
            }
            for order in orders
        ]

        write_file( self.file_path, rows, ORDER_FIELDNAMES)