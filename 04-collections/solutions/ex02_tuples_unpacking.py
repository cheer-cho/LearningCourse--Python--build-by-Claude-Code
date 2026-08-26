def min_max(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)


def head_tail(items: list[int]) -> tuple[int, list[int]]:
    first, *rest = items
    return first, rest


def distance(p: tuple[float, float], q: tuple[float, float]) -> float:
    x1, y1 = p
    x2, y2 = q
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
