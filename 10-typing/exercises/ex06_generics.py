# Scenario: a couple of "any type of list" helpers, plus a one-item
# container. Every function/method already works — add type annotations
# only, using a classic `TypeVar` (the exercises use classic TypeVar
# syntax; the LESSON also shows the newer `def f[T]()` shorthand).
# Concepts: `TypeVar`, generic functions, `Generic[T]` classes.
# Run: uv run pytest 10-typing -k ex06

from typing import Generic, TypeVar

T = TypeVar("T")


def first(items):
    """Add type hints: `items` is a list of any single type T, and the
    result is that same T. Assumes `items` is non-empty.

    first([1, 2, 3]) -> 1
    first(["a", "b"]) -> "a"
    """
    return items[0]


def last_or(items, default):
    """Add type hints: `items` is a list of T, `default` is a T, result
    is T.

    Return the last item of `items`, or `default` if it's empty.

    last_or([1, 2, 3], 0) -> 3
    last_or([], 0) -> 0
    """
    if items:
        return items[-1]
    return default


class Box(Generic[T]):  # noqa: UP046 — classic TypeVar syntax, see LESSON.md
    """Add type hints to `__init__`, `get`, and `put` so the box's
    contents stay whatever type T it was created with.

    A container holding exactly one value.

    box = Box(5); box.get() -> 5
    box.put(6); box.get() -> 6

    # Type-error probe (proves T is really enforced, not just `Any`) —
    # this is checked by the mypy test in test_ex06_generics.py, not run
    # here:
    #     int_box: Box[int] = Box(5)
    #     int_box.put("not an int")   # mypy should flag this
    """

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def put(self, value):
        self.value = value
