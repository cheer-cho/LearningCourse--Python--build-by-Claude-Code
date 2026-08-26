# Scenario: a tiny user directory with lookups that might come up empty,
# plus a value that can be one of two shapes. Every function already
# works — add type annotations only. Concepts: `T | None`, `X | Y`
# unions, and narrowing (`is None` checks, `isinstance`).
# Run: uv run pytest 10-typing -k ex03


def find_user(users, name):
    """Add type hints: `users` is a list of dicts shaped like
    {"name": str, ...}; return the matching dict or `None` if not found.

    Search `users` for the first dict whose "name" field equals `name`.

    find_user([{"name": "Ada"}], "Ada") -> {"name": "Ada"}
    find_user([{"name": "Ada"}], "Bo") -> None
    """
    for user in users:
        if user["name"] == name:
            return user
    return None


def describe(x):
    """Add type hints: `x` can be an int or a str; result is always str.

    Use `isinstance` to tell the two apart and describe `x` accordingly.

    describe(5) -> "int: 5"
    describe("hi") -> "str: 'hi'"
    """
    if isinstance(x, int):
        return f"int: {x}"
    return f"str: '{x}'"


def first_non_none(a, b):
    """Add type hints: both params are ints-or-None; result is always
    int. Assumes at least one of `a`, `b` is not None.

    Return `a` if it isn't None, otherwise fall back to `b`.

    first_non_none(None, 3) -> 3
    first_non_none(5, None) -> 5
    """
    if a is not None:
        return a
    assert b is not None
    return b
