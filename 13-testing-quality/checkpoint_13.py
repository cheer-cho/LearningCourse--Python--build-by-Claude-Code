# Checkpoint 13 — Cover the legacy function
#
# `shipping_quote` below is a gnarly, already-working function you did
# NOT write (given, fully implemented) and must not change. It's
# instrumented: every branch it takes adds a label to the module-level
# `BRANCHES_HIT` set. Your job is to choose test inputs — not touch the
# function — that make every branch run at least once. This combines
# everything in the module: case tables, parametrize thinking, and
# deliberate edge-case coverage.
# Run: uv run pytest 13-testing-quality -k checkpoint

BRANCHES_HIT: set[str] = set()

BRANCH_LABELS: set[str] = {
    "weight_light",
    "weight_medium",
    "weight_heavy",
    "domestic",
    "international",
    "free_domestic_shipping",
    "express",
    "standard",
    "fragile",
    "not_fragile",
}


def _hit(label: str) -> None:
    BRANCHES_HIT.add(label)


def shipping_quote(order: dict) -> float:
    """Given — fully implemented, do not modify. Computes a shipping
    cost from an order dict with keys: subtotal (float), weight_kg
    (float), international (bool), express (bool), fragile (bool).

    Rules, applied in this order:
    1. Base rate by weight: < 1kg -> 5.0, 1kg to <5kg -> 10.0, >= 5kg -> 20.0.
    2. International orders double the base rate so far.
    3. Domestic orders (not international) with subtotal >= 100 get
       free shipping: base becomes 0.0 (this OVERRIDES step 1's rate,
       but international orders never qualify, no matter the subtotal).
    4. Express adds a flat 15.0.
    5. Fragile adds a flat 5.0.

    shipping_quote({"subtotal": 20.0, "weight_kg": 0.5, "international": False, "express": False, "fragile": False}) -> 5.0
    shipping_quote({"subtotal": 150.0, "weight_kg": 2.0, "international": False, "express": False, "fragile": False}) -> 0.0
    """
    weight = order["weight_kg"]
    subtotal = order["subtotal"]
    international = order["international"]
    express = order["express"]
    fragile = order["fragile"]

    if weight < 1:
        base = 5.0
        _hit("weight_light")
    elif weight < 5:
        base = 10.0
        _hit("weight_medium")
    else:
        base = 20.0
        _hit("weight_heavy")

    if international:
        base *= 2
        _hit("international")
    else:
        _hit("domestic")

    if subtotal >= 100 and not international:
        base = 0.0
        _hit("free_domestic_shipping")

    if express:
        base += 15.0
        _hit("express")
    else:
        _hit("standard")

    if fragile:
        base += 5.0
        _hit("fragile")
    else:
        _hit("not_fragile")

    return base


# TODO: fill this in. Each dict needs the five `shipping_quote` input
# keys plus "expected" (the total you worked out by hand). Choose
# inputs deliberately so that, all together, every label in
# BRANCH_LABELS gets added to BRANCHES_HIT by the time every case (plus
# `make_edge_order()`) has run through `shipping_quote` once.
QUOTE_CASES: list[dict] = [
    {
        "subtotal": 0.0,
        "weight_kg": 0.5,
        "international": False,
        "express": False,
        "fragile": False,
        "expected": 999.0,
    },
]


def make_edge_order() -> dict:
    """Return an order dict (same shape as the `QUOTE_CASES` entries,
    minus "expected") for the single nastiest combination: heavy AND
    international AND express AND fragile, with a subtotal high enough
    that it WOULD qualify for free shipping if it weren't international
    — proving free-shipping correctly never applies internationally.

    make_edge_order() -> {"subtotal": 500.0, "weight_kg": 9.0, "international": True, "express": True, "fragile": True}
    """
    raise NotImplementedError
