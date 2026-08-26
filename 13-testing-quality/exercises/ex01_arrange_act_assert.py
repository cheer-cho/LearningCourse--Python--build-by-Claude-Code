# Scenario: an order-processing system needs test data built the same
# way everywhere, and a helper for writing readable custom assertions.
# Concepts: arrange/act/assert, factory functions, one behavior per test.
# Run: uv run pytest 13-testing-quality -k ex01

from dataclasses import dataclass


@dataclass
class Order:
    """A single order line. Given — not part of the exercise."""

    id: int
    item: str
    quantity: int
    unit_price: float
    paid: bool = False


def make_order(**overrides: object) -> Order:
    """Return an `Order` with sensible defaults, overridden by any
    keyword arguments given. This is the "arrange" step every test in
    this file (and the meta-tests) reuses instead of repeating.

    Defaults: id=1, item="widget", quantity=1, unit_price=9.99, paid=False.

    make_order() -> Order(id=1, item="widget", quantity=1, unit_price=9.99, paid=False)
    make_order(quantity=3) -> same order but quantity=3, everything else default
    """
    raise NotImplementedError


def make_paid_order(**overrides: object) -> Order:
    """Like `make_order`, but the returned order always has `paid=True`
    — even if the caller passes `paid=False` as an override (this
    factory's whole point is "give me an order that's definitely paid").

    make_paid_order() -> Order(..., paid=True)
    make_paid_order(paid=False) -> Order(..., paid=True)  # still True
    """
    raise NotImplementedError


def describe_failure(expected: object, actual: object) -> str:
    """Return a one-line, human-readable message for a custom assertion
    failure. The message must contain the word "expected", either "got"
    or "actual" (any case), and the `repr()` of both values, so a
    failure is scannable without a debugger.

    describe_failure(5, 3) -> "expected 5, got 3"  (exact wording is
        yours — must mention both values and both required words)
    """
    raise NotImplementedError
