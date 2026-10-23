"""Unit tests for ``FoodService``.

Run with:
    python -m pytest test/test_food_service.py -v

"""

import pytest

from src.models.food import Food
from src.services.food_service import FoodService

@pytest.fixture
def food_service() -> FoodService:

    #Build a FoodService with three known foods
    foods = [
        Food(101, "Burger", "Fast Food", 120.0, 75.0, 20, 5.0, 10.0, 4.5),
        Food(102, "Pizza", "Fast Food", 250.0, 150.0, 30, 5.0, 15.0, 4.7),
        Food(103, "Biryani", "Main Course", 180.0, 110.0, 40, 5.0, 5.0, 4.6),
    ]

    return FoodService(foods)

# ---------- search_food ----------

def test_search_food(food_service: FoodService)->None:
    """An exact name returns exactly one matching food."""
    search_foodName = "burger"
    results = food_service.search_food(search_foodName)

    assert len(results) == 1
    assert results[0].food_name.lower() == search_foodName.lower()


def test_search_food_no_match(food_service: FoodService)->None:
    """A keyword that matches nothing returns an empty list."""
    search_foodName = " "
    result = food_service.search_food(search_foodName)

    assert result == []

# ---------- find_food_by_id ----------

def test_find_food_by_id(food_service: FoodService)->None:
    """An existing ID returns the matching Food object."""
    food_id = 101
    result = food_service.find_food_by_id(food_id)
    
    assert result is not None
    assert result.food_id == food_id


def test_find_food_by_id_not_matched(food_service: FoodService)->None:
    """An unknown ID returns None (not an empty dict)."""
    food_id = 10111
    result = food_service.find_food_by_id(food_id)

    assert result is None

# ---------- max / min price ----------
def test_find_maximum_price(food_service: FoodService) -> None:
    """The highest priced food is Pizza."""
    result = food_service.find_maximum_price()
 
    assert result is not None
    assert result.food_name == "Pizza"
 
 
def test_find_minimum_price(food_service: FoodService) -> None:
    """The lowest priced food is Burger."""
    result = food_service.find_minimum_price()
 
    assert result is not None
    assert result.food_name == "Burger"
 
 
def test_max_min_price_with_empty_list() -> None:
    """With no foods, both price lookups return None instead of raising."""
    empty_service = FoodService([])
 
    assert empty_service.find_maximum_price() is None
    assert empty_service.find_minimum_price() is None

    