# Scenario: a scoreboard app that ranks, inserts, and filters raw score
# lists. Concepts: indexing, slicing, append/insert/remove/pop, `in`,
# `len`, sorted() vs .sort().
# Run: uv run pytest 04-collections -k ex01


def top_three(scores: list[int]) -> list[int]:
    """Return the 3 highest scores, highest first.

    Does not modify `scores`. If `scores` has fewer than 3 items, return
    all of them (still sorted highest first).

    top_three([50, 90, 10, 100, 70]) -> [100, 90, 70]
    top_three([5, 1]) -> [5, 1]
    """
    raise NotImplementedError


def insert_sorted(items: list[int], x: int) -> list[int]:
    """Insert `x` into `items` (assumed already sorted ascending) so the
    list stays sorted, then return the same list.

    insert_sorted([1, 3, 5], 4) -> [1, 3, 4, 5]
    insert_sorted([1, 3, 5], 0) -> [0, 1, 3, 5]
    insert_sorted([], 7) -> [7]
    """
    raise NotImplementedError


def without_negatives(nums: list[int]) -> list[int]:
    """Return a new list containing only the non-negative numbers from
    `nums`, in their original order. Write this with a plain `for` loop —
    comprehensions arrive in ex06.

    without_negatives([3, -1, 0, -5, 2]) -> [3, 0, 2]
    without_negatives([-1, -2]) -> []
    """
    raise NotImplementedError
