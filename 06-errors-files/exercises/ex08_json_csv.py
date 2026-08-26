# Scenario: saving app settings as JSON and reading a warehouse
# inventory from CSV. Concepts: `json.dump`/`json.load` roundtrips,
# `csv.DictReader`, converting CSV strings to the right type.
# Run: uv run pytest 06-errors-files -k ex08

import csv  # noqa: F401 — needed once save_config/load_config/read_inventory are implemented
import json  # noqa: F401 — needed once save_config/load_config/read_inventory are implemented


def save_config(path, config):
    """Write `config` (a dict) to `path` as JSON.

    Use `json.dump` with `with open(path, "w", encoding="utf-8") as f`.

    save_config(path, {"debug": True}) -> file at `path` contains valid
    JSON for {"debug": True}
    """
    raise NotImplementedError


def load_config(path):
    """Read the JSON file at `path` and return it as a dict.

    Use `json.load` with `with open(path, encoding="utf-8") as f`.

    file containing '{"debug": true}' -> load_config(path) == {"debug": True}
    """
    raise NotImplementedError


def read_inventory(path):
    """Read a CSV file at `path` with columns "name" and "quantity" into
    a list of dicts, one per row, with "quantity" converted to int.

    Use `csv.DictReader`. Every other column stays a str.

    CSV:
        name,quantity
        bolts,100
        screws,250
    -> [{"name": "bolts", "quantity": 100}, {"name": "screws", "quantity": 250}]
    """
    raise NotImplementedError
