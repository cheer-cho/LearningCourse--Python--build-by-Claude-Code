import json
import os
from pathlib import Path


def read_api_key() -> str:
    key = os.environ.get("API_KEY", "")
    if not key:
        raise RuntimeError("API_KEY is not set")
    return key


def cache_result(path: Path, key: str, value: str) -> None:
    data: dict[str, str] = {}
    if path.exists():
        data = json.loads(path.read_text())
    data[key] = value
    path.write_text(json.dumps(data))


def cached(path: Path, key: str) -> str | None:
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return data.get(key)
