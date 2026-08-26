# Scenario: small inventory/roster helpers. Every function already works —
# add type annotations only. Concepts: `list[T]`, `dict[K, V]`, fixed
# `tuple[str, int]`, variadic `tuple[int, ...]`.
# Run: uv run pytest 10-typing -k ex02


def total(prices):
    """Add type hints: `prices` is a list of floats, result is a float.

    Return the sum of every price.

    total([1.5, 2.0, 0.5]) -> 4.0
    total([]) -> 0.0
    """
    return sum(prices)


def index_by_name(users):
    """Add type hints: `users` is a list of dicts shaped like
    {"name": str, ...other fields}; return maps each user's name to
    their whole dict.

    Build a lookup keyed by each user's "name" field.

    index_by_name([{"name": "Ada", "age": 36}])
        -> {"Ada": {"name": "Ada", "age": 36}}
    """
    return {str(user["name"]): user for user in users}


def pair():
    """Add type hints: no params, returns a fixed 2-tuple (name, age).

    Return a hardcoded (name, age) pair.

    pair() -> ("Grace", 85)
    """
    return ("Grace", 85)


def scores_tuple(*scores):
    """Add type hints: `*scores` are individual int arguments; return
    them bundled as a variadic tuple, in order.

    Collect variadic positional args into a tuple.

    scores_tuple(1, 2, 3) -> (1, 2, 3)
    scores_tuple() -> ()
    """
    return scores
