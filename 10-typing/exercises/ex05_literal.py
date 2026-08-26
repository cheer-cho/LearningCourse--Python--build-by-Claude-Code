# Scenario: score sorting and a weekday helper. Every function already
# works — add type annotations only. Concepts: `Literal[...]` restricting
# a param to specific string values, a `Literal` type alias, exhaustive
# `match` handling.
# Run: uv run pytest 10-typing -k ex05

from typing import Literal

Weekday = Literal["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def sort_scores(scores, direction):
    """Add type hints: `scores` is a list of ints; `direction` is only
    ever "asc" or "desc" (use `Literal["asc", "desc"]`); result is
    list[int].

    Sort `scores` ascending or descending depending on `direction`.

    sort_scores([3, 1, 2], "asc") -> [1, 2, 3]
    sort_scores([3, 1, 2], "desc") -> [3, 2, 1]
    """
    if direction == "asc":
        return sorted(scores)
    return sorted(scores, reverse=True)


def day_number(day):
    """Add type hints: `day` is a Weekday, result is int (Mon=1 ... Sun=7).

    Every Weekday value is handled below — no catch-all `case _` needed,
    mypy can see the match is already exhaustive over the Literal.

    day_number("Mon") -> 1
    day_number("Sun") -> 7
    """
    match day:
        case "Mon":
            return 1
        case "Tue":
            return 2
        case "Wed":
            return 3
        case "Thu":
            return 4
        case "Fri":
            return 5
        case "Sat":
            return 6
        case "Sun":
            return 7
