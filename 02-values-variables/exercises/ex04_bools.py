"""ex04 — Booleans: comparisons, chained comparisons, is vs ==.

Scenario: yes/no checks on values. Covers comparison operators,
chained comparisons, and the difference between `is` (identity) and
`==` (equality).

Check: uv run python scripts/test.py 2 -k ex04
"""

from __future__ import annotations


def is_teen(age: int) -> bool:
    """True if age is a teenager's age (13 through 19 inclusive).

    Use a chained comparison: `13 <= age <= 19`.

    is_teen(13) -> True
    is_teen(19) -> True
    is_teen(20) -> False
    is_teen(5) -> False
    """
    if age >= 13 and age <= 19:
        return True
    return False


def same_object(a: object, b: object) -> bool:
    """True if `a` and `b` are the SAME object in memory (`is`).

    same_object([1, 2], [1, 2]) -> False  (equal values, different lists)
    """
    if a is b:
        return True
    return False


def same_value(a: object, b: object) -> bool:
    """True if `a` and `b` are equal in VALUE (`==`), regardless of identity.

    same_value([1, 2], [1, 2]) -> True  (different lists, same contents)
    """
    if a == b:
        return True
    return False
