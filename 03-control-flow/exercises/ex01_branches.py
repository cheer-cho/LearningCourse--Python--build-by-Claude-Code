# Scenario: a small storefront needs a grade report card and a shipping
# calculator. Covers: if/elif/else chains, nested decisions.
# Run: uv run pytest 03-control-flow -k ex01


def grade(score: float) -> str:
    """Convert a numeric score to a letter grade with an elif chain.

    Bands: A >= 90, B >= 80, C >= 70, D >= 60, else F.

    score -> letter
    95 -> "A"
    82 -> "B"
    59 -> "F"
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def shipping_cost(subtotal: float, express: bool) -> float:
    """Work out a shipping fee with a nested decision.

    Orders of $50 or more ship free standard, or for $4.99 express.
    Orders under $50 cost $5.99 standard, or $14.99 express.

    subtotal, express -> cost
    60, False -> 0.0
    60, True -> 4.99
    20, False -> 5.99
    20, True -> 14.99
    """
    if subtotal >= 50:
        return 4.99 if express else 0.0

    return 14.99 if express else 5.99
