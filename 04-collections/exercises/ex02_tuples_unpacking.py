# Scenario: a tiny geometry/stats helper library. Concepts: tuples as
# fixed-shape bundles, immutability, multiple assignment, starred
# unpacking.
# Run: uv run pytest 04-collections -k ex02


def min_max(nums: list[int]) -> tuple[int, int]:
    """Return a (lowest, highest) tuple for `nums`.

    `nums` has at least one item.

    min_max([3, 1, 4, 1, 5]) -> (1, 5)
    min_max([7]) -> (7, 7)
    """
    raise NotImplementedError


def head_tail(items: list[int]) -> tuple[int, list[int]]:
    """Split `items` into its first element and the rest, using starred
    unpacking (`first, *rest = items`). `items` has at least one item.

    head_tail([1, 2, 3]) -> (1, [2, 3])
    head_tail([9]) -> (9, [])
    """
    raise NotImplementedError


def distance(p: tuple[float, float], q: tuple[float, float]) -> float:
    """Return the straight-line distance between 2D points `p` and `q`,
    unpacking each tuple into its x, y parts.

    distance((0, 0), (3, 4)) -> 5.0
    """
    raise NotImplementedError
