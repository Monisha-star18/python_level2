import os
from pathlib import Path

from dotenv import load_dotenv

# Project root = folder that contains main.py (one level above /src)
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


def _resolve(value: str) -> Path:
    """Resolve a path from .env relative to the project root."""
    path = Path(value)
    return path if path.is_absolute() else BASE_DIR / path


def get_foodPath() -> Path:
    return _resolve(os.getenv("FOOD_PATH", "data/foods.json"))


def get_orderPath() -> Path:
    return _resolve(os.getenv("ORDER_PATH", "data/orders.json"))
