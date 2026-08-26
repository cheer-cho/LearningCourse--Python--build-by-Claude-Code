# Scenario: classic recursion drills — a base case plus a smaller
# version of the same problem. Concepts: base case, recursive case,
# the call stack.
# Run: uv run pytest 05-functions -k ex08


def sum_digits(n):
    """Return the sum of the decimal digits of non-negative int `n`,
    computed recursively (no loops, no `str(n)`).

    Base case: a single digit (n < 10) sums to itself.
    Recursive case: the last digit (n % 10) plus the sum of the digits
    of everything before it (n // 10).

    sum_digits(1234) -> 10
    sum_digits(7) -> 7
    sum_digits(0) -> 0
    """
    raise NotImplementedError


def flatten(nested):
    """Return a new flat list containing every non-list element of
    `nested`, in order, no matter how deeply the lists are nested,
    computed recursively.

    Base case: a non-list element becomes a single-item result.
    Recursive case: a list element gets flattened and the pieces
    stitched together.

    flatten([1, [2, 3, [4], []], 5]) -> [1, 2, 3, 4, 5]
    flatten([1, 2, 3]) -> [1, 2, 3]
    flatten([[[[1]]], 2]) -> [1, 2]
    """
    raise NotImplementedError


def count_down_up(n):
    """Build and return a string counting down from `n` to 1 and back
    up to `n`, space-separated, computed recursively. `n` is at least 1.

    Base case: count_down_up(1) -> "1 1"
    Recursive case: f"{n} {count_down_up(n - 1)} {n}"

    count_down_up(1) -> "1 1"
    count_down_up(3) -> "3 2 1 1 2 3"
    """
    raise NotImplementedError
