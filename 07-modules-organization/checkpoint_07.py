# Checkpoint 07 — Warehouse inventory package
#
# checkpoint_07_pkg/ is a tiny inventory package split into
# inventory.py (stock operations) and reports.py (reporting), both
# thin wrappers that import from THIS file — the same "_impl" pattern
# as ex03's mod07_shop package. Edit checkpoint_07.py, not the package
# files under checkpoint_07_pkg/; they're already correctly wired.
# An inventory is a dict[str, int], e.g. {"bolts": 40, "nuts": 5}.
# Run: uv run pytest 07-modules-organization -k checkpoint


def add_item(inventory, name, qty):
    """Add `qty` units of `name` to `inventory`, mutating it in place.
    Creates the entry if `name` isn't already a key. Returns nothing.

    inventory = {}
    add_item(inventory, "bolts", 40)  -> inventory is now {"bolts": 40}
    add_item(inventory, "bolts", 10)  -> inventory is now {"bolts": 50}
    """
    raise NotImplementedError


def remove_item(inventory, name, qty):
    """Remove `qty` units of `name` from `inventory`, mutating it in
    place. If the remaining quantity hits 0, delete the key entirely.
    Raises `ValueError` if `name` isn't in `inventory`, or if `qty` is
    more than the current stock. Returns nothing.

    inventory = {"bolts": 40}
    remove_item(inventory, "bolts", 15) -> inventory is now {"bolts": 25}
    remove_item(inventory, "bolts", 25) -> inventory is now {} (key removed)
    """
    raise NotImplementedError


def stock_count(inventory, name):
    """Return the current quantity of `name` in `inventory`, or 0 if
    `name` isn't a key (never raises `KeyError`).

    stock_count({"bolts": 40}, "bolts") -> 40
    stock_count({"bolts": 40}, "screws") -> 0
    """
    raise NotImplementedError


def low_stock_report(inventory, threshold):
    """Return the names of every item whose quantity is strictly below
    `threshold`, sorted alphabetically.

    low_stock_report({"bolts": 40, "nuts": 5, "screws": 2}, 10)
        -> ["nuts", "screws"]
    """
    raise NotImplementedError
