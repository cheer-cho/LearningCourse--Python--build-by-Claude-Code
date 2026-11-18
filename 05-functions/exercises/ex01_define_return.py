# Scenario: the smallest possible functions — define, return a value,
# and the classic bug of forgetting to. Concepts: def/return, returning
# multiple values as a tuple, implicit None.
# Run: uv run pytest 05-functions -k ex01


def rectangle_info(width: float, height: float) -> tuple[float, float]:
    """Return a (area, perimeter) tuple for a rectangle.

    area = width * height
    perimeter = 2 * (width + height)

    rectangle_info(3, 4) -> (12, 14)
    rectangle_info(5, 5) -> (25, 20)
    """
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


def clamp(value: float, lo: float, hi: float) -> float:
    """Return `value` restricted to the range [lo, hi].

    If `value` is below `lo`, return the number stored in `lo` (the
    lower bound). If it's above `hi`, return the number stored in `hi`
    (the upper bound). Otherwise return `value` unchanged. All three
    branches return a number, never a string.

    clamp(5, 0, 10) -> 5
    clamp(-3, 0, 10) -> 0
    clamp(99, 0, 10) -> 10
    """
    # oneliner
    # return max(lo, min(value, hi))

    if value < lo:
        return lo
    elif value > hi:
        return hi
    else:
        return value


def greet_missing_return(name: str) -> str:
    """BUG: this should build a greeting and return it, but it forgets
    the `return` keyword — the function runs fine and produces the
    right string, then throws it away, so the caller always gets back
    `None`. Add the missing `return`.

    greet_missing_return("Ada") -> "Hello, Ada!"
    """
    return f"Hello, {name}!"
