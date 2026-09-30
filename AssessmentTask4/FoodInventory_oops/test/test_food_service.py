import pytest

from src.models.food import Food
from src.services.food_service import FoodService

@pytest.fixture
def food_service() -> FoodService:
    foods = [
        Food(101, "Burger", "Fast Food", 120.0, 75.0, 20, 5.0, 10.0, 4.5),
        Food(102, "Pizza", "Fast Food", 250.0, 150.0, 30, 5.0, 15.0, 4.7),
        Food(103, "Biryani", "Main Course", 180.0, 110.0, 40, 5.0, 5.0, 4.6),
    ]

    food_service_object = FoodService(foods)

    return food_service_object


def test_search_food(food_service):

    search_foodName = "burger"

    results = food_service.search_food(search_foodName)

    assert len(results) == 1
    assert results[0].food_name.lower() == search_foodName.lower()


def test_search_food_no_match(food_service):

    search_foodName = " "

    result = food_service.search_food(search_foodName)

    assert result == []

    
def test_find_food_by_id(food_service):

    food_id = 101

    result = food_service.find_food_by_id(food_id)

    assert result.food_id == food_id


def test_find_food_by_id_not_matched(food_service):

    food_id = 10111

    result = food_service.find_food_by_id(food_id)

    assert result == {}

    