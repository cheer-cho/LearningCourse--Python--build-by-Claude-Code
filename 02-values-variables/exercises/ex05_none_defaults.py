"""ex05 — None and the conditional expression.

Scenario: filling in a placeholder when a value is missing. Covers
`None`, `is None`, and the one-liner conditional expression
`value_if_true if condition else value_if_false` — this is the ONLY
place in this module you're allowed to reach for it; full `if`
statements arrive in module 03.

Check: uv run python scripts/test.py 2 -k ex05
"""

from __future__ import annotations


def label_or_default(label: str | None) -> str:
    """Return `label`, or "(none)" if `label is None`.

    Use a conditional expression: `label if label is not None else "(none)"`.

    label_or_default("Ada") -> "Ada"
    label_or_default(None) -> "(none)"
    """
    raise NotImplementedError


def first_non_none(a: object | None, b: object) -> object:
    """Return `a` unless it's None, in which case return `b`.

    A common pattern for "use this value, or fall back to that one."
    Use a conditional expression, same as `label_or_default`.

    first_non_none("Ada", "Unknown") -> "Ada"
    first_non_none(None, "Unknown") -> "Unknown"
    first_non_none(0, "Unknown") -> 0  (0 is not None, so keep it)
    """
    raise NotImplementedError
