def every_other(s: str) -> str:
    return s[::2]


def reversed_copy(items: list[int]) -> list[int]:
    return items[::-1]


def middle(items: list[int]) -> list[int]:
    return items[1:-1]


def rotate(items: list[int], n: int) -> list[int]:
    if not items:
        return []
    n = n % len(items)
    return items[n:] + items[:n]
