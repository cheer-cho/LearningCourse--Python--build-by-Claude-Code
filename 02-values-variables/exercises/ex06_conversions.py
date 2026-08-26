"""ex06 — Type conversions: int(), float(), str(), and their errors.

Scenario: parsing text input into numbers. Covers `int()`, `float()`,
`str()`, string cleanup before conversion, and letting `ValueError`
propagate on bad input (no try/except yet — that's module 06).

Check: uv run python scripts/test.py 2 -k ex06
"""

from __future__ import annotations


def parse_price(text: str) -> float:
    """Parse a "$"-prefixed price string into a float.

    Strip whitespace and a leading "$", then convert to float. Garbage
    input should raise ValueError naturally — don't catch it.

    parse_price("$3.50") -> 3.5
    parse_price(" $12.00 ") -> 12.0
    parse_price("9.99") -> 9.99
    parse_price("free") -> raises ValueError
    """
    raise NotImplementedError


def age_next_year(age_text: str) -> int:
    """Parse a text age and return next year's age.

    Convert to int, then add 1. Garbage input should raise ValueError
    naturally — don't catch it.

    age_next_year("41") -> 42
    age_next_year("0") -> 1
    age_next_year("old") -> raises ValueError
    """
    raise NotImplementedError
