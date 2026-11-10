# Scenario: text/list utilities that lean entirely on slicing. Concepts:
# s[start:stop:step], reversal with [::-1], slice-copy vs alias.
# Run: uv run pytest 04-collections -k ex05


def every_other(s: str) -> str:
    """Return every other character of `s`, starting with the first.

    every_other("PYTHON") -> "PTO"
    every_other("") -> ""
    """
    return s[::2]


def reversed_copy(items: list[int]) -> list[int]:
    """Return a new list with `items` in reverse order. `items` itself
    must be unchanged afterwards.

    reversed_copy([1, 2, 3]) -> [3, 2, 1]
    """
    return items[::-1]


def middle(items: list[int]) -> list[int]:
    """Return `items` with the first and last elements dropped.

    middle([1, 2, 3, 4, 5]) -> [2, 3, 4]
    middle([1, 2]) -> []
    """
    return items[1:-1]


def rotate(items: list[int], n: int) -> list[int]:
    """Return a new list with `items` rotated left by `n` positions,
    using two slices joined together. `n` may be 0, and may be larger
    than `len(items)` (wrap around with `%`).

    rotate([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
    rotate([1, 2, 3], 0) -> [1, 2, 3]
    rotate([1, 2, 3], 4) -> [2, 3, 1]
    """
    if not items:
        return []

    n = n % len(items)
    return items[n:] + items[:n]
