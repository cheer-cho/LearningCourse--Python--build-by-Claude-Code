# Scenario: default parameter values — the safe kind (numbers) and the
# dangerous kind (mutable objects). Concepts: default arguments,
# def-time-vs-call-time evaluation, the None-sentinel fix.
# Run: uv run pytest 05-functions -k ex02


def power(base, exp=2):
    """Return `base` raised to `exp`. `exp` defaults to squaring.

    power(3) -> 9
    power(2, 5) -> 32
    power(7, 0) -> 1
    """
    raise NotImplementedError


def add_item(item, items=[]):
    """BUG: append `item` to `items` and return `items`. When the
    caller doesn't pass `items`, each call is supposed to start from a
    fresh, empty list — but a mutable default value is created ONCE,
    when Python reads this `def`, not once per call. As written, every
    call that omits `items` appends to the SAME list, so calls leak
    into each other. Fix it with the None-sentinel pattern: default
    `items` to `None`, then build a real empty list inside the body
    when it's still `None`.

    add_item(1) -> [1]
    add_item(2, [1]) -> [1, 2]
    # two separate calls with no `items` must NOT share state:
    add_item("a") -> ["a"]
    add_item("b") -> ["b"]      # NOT ["a", "b"]
    """
    items.append(item)
    return items
