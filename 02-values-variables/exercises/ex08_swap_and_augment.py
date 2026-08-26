"""ex08 — Tuple swap, augmented assignment, and operator precedence.

Scenario: rearranging and updating values without loops or temp
variables. Covers tuple assignment, augmented assignment (`+=` etc.),
and operator precedence.

Check: uv run python scripts/test.py 2 -k ex08
"""

from __future__ import annotations


def swap(a: object, b: object) -> tuple[object, object]:
    """Return the pair swapped, using tuple assignment (no temp variable).

    swap(1, 2) -> (2, 1)
    swap("x", "y") -> ("y", "x")
    """
    raise NotImplementedError


def apply_raise_and_bonus(salary: float, raise_amount: float, bonus: float) -> float:
    """Give a salary a raise, then add a flat bonus.

    Use augmented assignment (`+=`) for both steps instead of writing
    `salary = salary + ...` twice.

    apply_raise_and_bonus(50000.0, 2000.0, 500.0) -> 52500.0
    apply_raise_and_bonus(100.0, 0.0, 10.0) -> 110.0
    """
    raise NotImplementedError


def evaluate() -> int:
    """Precedence puzzle: add parentheses to hit the target value.

    `*` binds tighter than `+`, so `2 + 3 * 4` evaluates to 14, not 20.
    Without changing the numbers or operators, add ONE pair of
    parentheses so the expression evaluates to 20.

    evaluate() -> 20
    """
    # TODO: add parentheses below — this currently returns 14, not 20.
    return 2 + 3 * 4
