import json
from pathlib import Path


def write_file(path: Path, rows: list[dict], fieldnames: list[str] | None = None) -> None:

    with path.open(mode="w", encoding="utf-8") as file:
        json.dump(rows, file, indent=2)