import csv
from pathlib import Path


def read_file(path: Path) -> list[dict[str, str]]:

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open(mode="r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)
        return list(reader)
