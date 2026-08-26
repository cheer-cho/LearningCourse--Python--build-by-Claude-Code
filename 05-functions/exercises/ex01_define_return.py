# Scenario: the smallest possible functions — define, return a value,
# and the classic bug of forgetting to. Concepts: def/return, returning
# multiple values as a tuple, implicit None.
# Run: uv run pytest 05-functions -k ex01


def rectangle_info(width, height):
    """Return a (area, perimeter) tuple for a rectangle.

    area = width * height
    perimeter = 2 * (width + height)

    rectangle_info(3, 4) -> (12, 14)
    rectangle_info(5, 5) -> (25, 20)
    """
    raise NotImplementedError


def clamp(value, lo, hi):
    """Return `value` restricted to the range [lo, hi].

    If `value` is below `lo`, return `lo`. If it's above `hi`, return
    `hi`. Otherwise return `value` unchanged.

    clamp(5, 0, 10) -> 5
    clamp(-3, 0, 10) -> 0
    clamp(99, 0, 10) -> 10
    """
    raise NotImplementedError


def greet_missing_return(name):
    """BUG: this should build a greeting and return it, but it forgets
    the `return` keyword — the function runs fine and produces the
    right string, then throws it away, so the caller always gets back
    `None`. Add the missing `return`.

    greet_missing_return("Ada") -> "Hello, Ada!"
    """
    message = f"Hello, {name}!"
    # BUG: no return statement here — falls off the end, returns None
