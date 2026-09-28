import csv
from pathlib import Path


def write_file(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:

    with path.open(mode="w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
