from dataclasses import dataclass
from datetime import date

@dataclass
class Order:

    order_id: int
    customer_name: str
    food_id: int
    quantity: int
    order_date: date
    status: str
    payment_method: str