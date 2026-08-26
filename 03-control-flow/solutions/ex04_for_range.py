# Reference solution for ex04_for_range — see exercises/ex04_for_range.py
# for the scenario.


def sum_multiples(limit: int, k: int) -> int:
    """Sum every positive multiple of k that is strictly less than limit.

    Built with range(k, limit, k) — start at the first multiple, stop
    before limit, step by k.

    limit, k -> result
    10, 3 -> 18   (3 + 6 + 9)
    20, 5 -> 30   (5 + 10 + 15)
    5, 10 -> 0    (no multiples of 10 below 5)
    """
    total = 0
    for multiple in range(k, limit, k):
        total += multiple
    return total


def factorial(n: int) -> int | None:
    """Compute n! with a for loop over range(2, n + 1).

    Guards n < 0 by returning None (factorial isn't defined there).

    n -> result
    0 -> 1
    5 -> 120
    -1 -> None
    """
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def stripes(n: int) -> str:
    """Build an alternating "=-=-=" style string of length n.

    Even indices (0, 2, 4, ...) get "=", odd indices get "-", found with
    range(n) and i % 2.

    n -> result
    5 -> "=-=-="
    1 -> "="
    0 -> ""
    """
    result = ""
    for i in range(n):
        if i % 2 == 0:
            result += "="
        else:
            result += "-"
    return result
