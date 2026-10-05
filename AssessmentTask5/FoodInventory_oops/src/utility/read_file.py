import asyncio, json
from pathlib import Path


def _read_sync(path: Path) -> list[dict]:

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open(mode="r", encoding="utf-8") as file:
        return json.load(file)

async def read_file(path: Path) -> list[dict]:
    return await asyncio.to_thread(_read_sync, path)