# Scenario: shapes from unrelated libraries that all happen to have an
# `area()` method. Concepts: `Protocol` (structural typing — "this is TS
# interfaces"), annotating with `Iterable[...]`.
# Run: uv run pytest 10-typing -k ex07

import math
from collections.abc import Iterable
from typing import Protocol


class HasArea(Protocol):
    """Anything with an `area() -> float` method satisfies this —
    structurally, with no inheritance required.
    """

    def area(self) -> float: ...


class Circle:
    """A circle. Does NOT inherit from HasArea — Protocols are
    structural, so this still satisfies it.
    """

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


class Square:
    """A square. Also does NOT inherit from HasArea."""

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


def total_area(shapes: Iterable[HasArea]) -> float:
    """Sum the area of every shape.

    total_area([Circle(1.0)]) -> 3.14159...
    total_area([Square(2.0)]) -> 4.0
    """
    return sum(shape.area() for shape in shapes)
