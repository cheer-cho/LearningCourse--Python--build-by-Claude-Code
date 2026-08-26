# Scenario: small inventory/roster helpers. Every function already works —
# add type annotations only. Concepts: `list[T]`, `dict[K, V]`, fixed
# `tuple[str, int]`, variadic `tuple[int, ...]`.
# Run: uv run pytest 10-typing -k ex02


def total(prices: list[float]) -> float:
    """Return the sum of every price.

    total([1.5, 2.0, 0.5]) -> 4.0
    total([]) -> 0.0
    """
    return sum(prices)


def index_by_name(users: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    """Build a lookup keyed by each user's "name" field.

    index_by_name([{"name": "Ada", "age": 36}])
        -> {"Ada": {"name": "Ada", "age": 36}}
    """
    return {str(user["name"]): user for user in users}


def pair() -> tuple[str, int]:
    """Return a hardcoded (name, age) pair.

    pair() -> ("Grace", 85)
    """
    return ("Grace", 85)


def scores_tuple(*scores: int) -> tuple[int, ...]:
    """Collect variadic positional args into a tuple.

    scores_tuple(1, 2, 3) -> (1, 2, 3)
    scores_tuple() -> ()
    """
    return scores
