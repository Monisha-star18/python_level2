import json
from pathlib import Path


def read_file(path: Path) -> list[dict]:

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open(mode="r", encoding="utf-8") as file:
        return json.load(file)