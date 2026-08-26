"""ex01 — Numbers: arithmetic, floor division, and rounding.

Scenario: small money- and time-related calculations. Covers `+ - * /
// % **` and `round()`.

Check: uv run python scripts/test.py 2 -k ex01
"""

from __future__ import annotations


def minutes_to_hours_minutes(total_minutes: int) -> tuple[int, int]:
    """Split a total minute count into (hours, minutes).

    Use `//` (floor division) for the hours and `%` (modulo) for the
    leftover minutes.

    minutes_to_hours_minutes(125) -> (2, 5)
    minutes_to_hours_minutes(59) -> (0, 59)
    minutes_to_hours_minutes(180) -> (3, 0)
    """
    raise NotImplementedError


def apply_discount(price: float, percent_off: float) -> float:
    """Apply a percentage discount to a price, rounded to 2 decimals.

    percent_off is a number like 20 for "20% off". Use `round(..., 2)`
    so the result is a clean money value.

    apply_discount(50.0, 20) -> 40.0
    apply_discount(19.99, 10) -> 17.99
    """
    raise NotImplementedError


def power_area(radius: float) -> float:
    """Area of a circle with the given radius, rounded to 2 decimals.

    Area = pi * radius ** 2. Use `math.pi` and the `**` operator.

    power_area(2) -> 12.57
    power_area(1) -> 3.14
    """
    raise NotImplementedError
