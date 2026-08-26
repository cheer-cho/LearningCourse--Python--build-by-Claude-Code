# Scenario: functions that remember state via closures, and the
# classic bug where a closure captures a loop variable by reference
# instead of by value. Concepts: closures, factory functions, the
# loop-capture trap.
# Run: uv run pytest 05-functions -k ex06


def make_multiplier(k):
    """Return a function of one argument, `n`, that returns `n * k`.
    Each call to `make_multiplier` must produce an independent
    closure — different `k` values must not interfere with each other.

    triple = make_multiplier(3)
    triple(5) -> 15
    triple(0) -> 0
    """
    raise NotImplementedError


def make_accumulator():
    """Return a function of one argument, `amount`, that adds `amount`
    to a running total (starting at 0) and returns the new total. Each
    call to `make_accumulator` must start its own independent total.

    acc = make_accumulator()
    acc(10) -> 10
    acc(5) -> 15
    acc(-3) -> 12
    """
    raise NotImplementedError


def make_button_handlers(labels):
    """BUG: this should return a list of zero-argument functions — one
    per label — where calling the Nth function returns
    f"{labels[N]} clicked (button {N})". As written, every closure
    captures the loop variables `i` and `label` BY REFERENCE, and all
    the closures share the exact same `i` and `label` cells. By the
    time any handler is actually called, the loop has already finished,
    so `i` and `label` are stuck at their FINAL values — every handler
    reports the last button, no matter which one you call. Fix it: bind
    the current `i` and `label` as default argument values
    (`def handler(i=i, label=label): ...`), which copies their CURRENT
    value into the new function at definition time. (A separate factory
    function that takes `i, label` as real parameters works too.)

    handlers = make_button_handlers(["Save", "Cancel", "Delete"])
    handlers[0]() -> "Save clicked (button 0)"
    handlers[1]() -> "Cancel clicked (button 1)"
    handlers[2]() -> "Delete clicked (button 2)"
    """
    handlers = []
    for i, label in enumerate(labels):

        def handler():
            return f"{label} clicked (button {i})"

        handlers.append(handler)
    return handlers
