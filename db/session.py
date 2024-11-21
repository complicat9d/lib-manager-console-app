import os
import json
from typing import Dict, Any
from contextlib import contextmanager

db_url = os.path.join(os.getcwd(), "db", "data.json")
os.makedirs(os.path.dirname(db_url), exist_ok=True)


@contextmanager
def get_session() -> Dict[str, Any]:
    """Context manager that simulates a session interacting with a JSON-based "database"."""
    if os.path.exists(db_url):
        with open(db_url, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    try:
        yield data

        with open(db_url, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Error during session: {e}")
        raise
