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


QUOTE_CASES: list[dict] = [
    # weight_light, domestic, standard, not_fragile
    {
        "subtotal": 20.0,
        "weight_kg": 0.5,
        "international": False,
        "express": False,
        "fragile": False,
        "expected": 5.0,
    },
    # weight_medium, domestic, free_domestic_shipping, express, fragile
    {
        "subtotal": 150.0,
        "weight_kg": 2.0,
        "international": False,
        "express": True,
        "fragile": True,
        "expected": 20.0,  # 0.0 (free) + 15.0 express + 5.0 fragile
    },
    # weight_heavy, international, standard, not_fragile, subtotal below
    # the free-shipping threshold (so it's clear that's not why it's paid)
    {
        "subtotal": 50.0,
        "weight_kg": 6.0,
        "international": True,
        "express": False,
        "fragile": False,
        "expected": 40.0,  # 20.0 base * 2 international
    },
]


def make_edge_order() -> dict:
    return {
        "subtotal": 500.0,
        "weight_kg": 9.0,
        "international": True,
        "express": True,
        "fragile": True,
    }
