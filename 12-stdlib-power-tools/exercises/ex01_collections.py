# Scenario: three collections-module helpers you'll reach for constantly
# once real data shows up — counting words, grouping records, and keeping
# a bounded window of recent items. Concepts: Counter, defaultdict, deque.
# Run: uv run pytest 12-stdlib-power-tools -k ex01

from collections import deque  # noqa: F401 — needed once LastN is implemented


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the `n` most common whitespace-separated words in `text`,
    as (word, count) pairs sorted by count descending. Ties break
    alphabetically so the result is deterministic regardless of
    Counter's internal ordering.

    top_words("a b b c c c", 2) -> [("c", 3), ("b", 2)]
    top_words("x x y y", 2) -> [("x", 2), ("y", 2)]
    """
    raise NotImplementedError


def group_by_first_letter(names: list[str]) -> dict[str, list[str]]:
    """Group `names` by their first character, preserving each name's
    original relative order within its group.

    group_by_first_letter(["Ada", "Al", "Bo"])
        -> {"A": ["Ada", "Al"], "B": ["Bo"]}
    """
    raise NotImplementedError


class LastN:
    """Keeps only the `n` most recently added items; the oldest item is
    dropped automatically once the deque is full. Backed by
    collections.deque(maxlen=n).

    keeper = LastN(2)
    keeper.add(1); keeper.add(2); keeper.add(3)
    keeper.items() -> [2, 3]
    """

    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def add(self, item: object) -> None:
        raise NotImplementedError

    def items(self) -> list[object]:
        raise NotImplementedError
