# Scenario: quick utility functions that lean on the standard library
# instead of reinventing math from scratch. Concepts: the three main
# import forms (`import x`, `from x import y`, `import x as z`) — one
# used by each function below.
# Run: uv run pytest 07-modules-organization -k ex01

import math  # noqa: F401 — needed once circle_area is implemented
import string as s  # noqa: F401 — needed once alphabet_position is implemented
from statistics import median  # noqa: F401 — needed once middle_value is implemented


def circle_area(radius):
    """Return the area of a circle with the given `radius`.

    Use `math.pi` (imported above with plain `import math`).

    circle_area(1) -> 3.141592653589793
    circle_area(0) -> 0.0
    """
    raise NotImplementedError


def middle_value(numbers):
    """Return the median of `numbers`.

    Use `median` (imported above with `from statistics import median`).
    `numbers` has at least one item.

    middle_value([3, 1, 2]) -> 2
    middle_value([1, 2, 3, 4]) -> 2.5
    """
    raise NotImplementedError


def alphabet_position(letter):
    """Return the 1-based position of a lowercase `letter` in the
    alphabet (`"a"` -> 1, `"z"` -> 26).

    Use `s.ascii_lowercase` (imported above with `import string as s`)
    and its `.index()` method.

    alphabet_position("a") -> 1
    alphabet_position("m") -> 13
    """
    raise NotImplementedError
