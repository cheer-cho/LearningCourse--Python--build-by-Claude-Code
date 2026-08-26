def pair_up(names, scores):
    """Pair each name with its score at the same position.

    pair_up(["Ada", "Bo"], [90, 70]) -> [("Ada", 90), ("Bo", 70)]
    pair_up([], []) -> []
    """
    return list(zip(names, scores))


def numbered_lines(lines):
    """Number each line starting at 1, as "N: text" strings.

    numbered_lines(["a", "b"]) -> ["1: a", "2: b"]
    numbered_lines([]) -> []
    """
    return [f"{position}: {line}" for position, line in enumerate(lines, start=1)]


def elementwise_diff(a, b):
    """Return the absolute difference between `a` and `b` at each
    shared position (extra items in the longer list are ignored).

    elementwise_diff([10, 20, 30], [1, 25, 30]) -> [9, 5, 0]
    elementwise_diff([], []) -> []
    """
    return [abs(x - y) for x, y in zip(a, b)]


def first_index_of(items, target):
    """Return the position of the first `target` in `items`, or -1 if
    it isn't there.

    first_index_of(["a", "b", "c"], "c") -> 2
    first_index_of(["a", "b"], "z") -> -1
    """
    return next((position for position, value in enumerate(items) if value == target), -1)
