from dataclasses import dataclass

@dataclass
class Food:

    food_id: int
    food_name: str
    category: str
    price: float
    cost_price: float
    stock_quantity: int
    tax_percent: float
    discount_percent: float
    rating: float

    @property
    def profit(self) -> float:
        return self.price - self.cost_price

    @property
    def discount_amount(self) -> float:
        return self.price * self.discount_percent / 100

    @property
    def tax_amount(self) -> float:
        return self.price * self.tax_percent / 100