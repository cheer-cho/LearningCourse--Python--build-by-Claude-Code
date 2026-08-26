"""ex07 — Aliasing: names are labels, not boxes.

Scenario: prediction drills. Each function below already contains the
code that runs — your job is NOT to write logic, it's to predict what
the mutated value looks like afterward and hard-code that literal as
the return value. Don't just `return a` — that would dodge the
prediction. Covers aliasing (two names, one object) vs rebinding (a
name pointing at a new object).

Check: uv run python scripts/test.py 2 -k ex07
"""

from __future__ import annotations


def shared_append() -> list[int]:
    """Predict what `a` is after this code runs, then hard-code it.

    a = [1, 2]
    b = a            # b is an alias for the SAME list, not a copy
    b.append(3)       # mutates the one list both names point at
    # what does `a` look like now?
    """
    a = [1, 2]
    b = a
    b.append(3)
    # TODO: replace this wrong guess with your prediction for `a`.
    return [1, 2]


def two_names_one_list() -> list[int]:
    """Predict what `b` is after this code runs, then hard-code it.

    a = [1, 2, 3]
    b = a            # b is an alias for the SAME list
    a.append(4)       # mutating through `a` is visible through `b` too
    # what does `b` look like now?
    """
    a = [1, 2, 3]
    b = a
    a.append(4)
    assert b is a  # same object — mutating through `a` shows up in `b` too
    # TODO: replace this wrong guess with your prediction for `b`.
    return [1, 2, 3]


def rebind_vs_alias() -> tuple[list[int], list[int]]:
    """Predict what `(a, b)` are after this code runs, then hard-code it.

    a = [1, 2]
    b = a            # alias: same list
    b = b + [3]       # `+` builds a NEW list; this REBINDS b, doesn't mutate
    # what do `a` and `b` look like now?
    """
    a = [1, 2]
    b = a
    b = b + [3]
    # TODO: replace this wrong guess with your prediction for `(a, b)`.
    return ([1, 2], [1, 2])
