import csv
import json


def save_config(path, config):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


def load_config(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def read_inventory(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["quantity"] = int(row["quantity"])
    return rows
