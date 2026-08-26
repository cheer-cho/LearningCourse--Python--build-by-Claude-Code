# ✦ CHECKPOINT 10 — Orders
#
# A small "orders" module. Every function and class below already works —
# your ONLY job is to make `uv run mypy --strict checkpoint_10.py` happy
# WITHOUT changing any behavior. That means: define `Order` and
# `HasTotal` (currently empty placeholders) with the right shape, and add
# every missing annotation. Combines everything from this module:
# TypedDict, Optional, generics, and Protocol.
# Run: uv run pytest 10-typing -k checkpoint

from typing import Protocol, TypedDict, TypeVar

T = TypeVar("T")


class Order(TypedDict):
    """Define this TypedDict's keys (all required):

    - id: str
    - item: str
    - qty: int
    - price: float
    """


class HasTotal(Protocol):
    """Define this Protocol: anything with a `total() -> float` method
    satisfies it — no inheritance required.
    """


# You'll need `from collections.abc import Iterable` once you annotate
# `sum_totals` below.


def order_total(order):
    """Add type hints: order is an Order, result is float.

    Return `qty * price` for one order.

    order_total({"id": "1", "item": "Mug", "qty": 2, "price": 5.0}) -> 10.0
    """
    return order["qty"] * order["price"]


def format_order(order):
    """Add type hints: order is an Order, result is str.

    Format an order as "QTYx ITEM ($TOTAL)", total to 2 decimal places.

    format_order({"id": "1", "item": "Mug", "qty": 2, "price": 5.0})
        -> "2x Mug ($10.00)"
    """
    return f"{order['qty']}x {order['item']} (${order_total(order):.2f})"


def filter_expensive(orders, threshold):
    """Add type hints: orders is a list of Order, threshold is float,
    result is list[Order].

    Return every order whose total is strictly greater than `threshold`,
    in their original order.

    filter_expensive([{"id": "1", "item": "Mug", "qty": 2, "price": 5.0}], 5.0)
        -> [{"id": "1", "item": "Mug", "qty": 2, "price": 5.0}]
    """
    return [order for order in orders if order_total(order) > threshold]


def group_by_item(orders):
    """Add type hints: orders is a list of Order, result maps each item
    name to the list of orders for that item.

    Group `orders` by their "item" field, preserving each group's
    relative order.

    group_by_item([{"id": "1", "item": "Mug", "qty": 1, "price": 5.0}])
        -> {"Mug": [{"id": "1", "item": "Mug", "qty": 1, "price": 5.0}]}
    """
    groups = {}
    for order in orders:
        groups.setdefault(order["item"], []).append(order)
    return groups


def first_or_none(items):
    """Add type hints: items is a list of any single type T; result is
    that T, or None if `items` is empty. This is a general-purpose
    generic helper — it knows nothing about orders.

    first_or_none([1, 2, 3]) -> 1
    first_or_none([]) -> None
    """
    if items:
        return items[0]
    return None


def cheapest(orders):
    """Add type hints: orders is a list of Order, result is Order or None.

    Return the order with the smallest total, or None if `orders` is
    empty. Reuses `first_or_none` on a sorted copy.

    cheapest([{"id": "1", "item": "Mug", "qty": 1, "price": 5.0},
              {"id": "2", "item": "Pen", "qty": 1, "price": 1.0}])
        -> {"id": "2", "item": "Pen", "qty": 1, "price": 1.0}
    cheapest([]) -> None
    """
    return first_or_none(sorted(orders, key=order_total))


def total_revenue(orders):
    """Add type hints: orders is a list of Order, result is float.

    Sum every order's total.

    total_revenue([{"id": "1", "item": "Mug", "qty": 2, "price": 5.0}]) -> 10.0
    total_revenue([]) -> 0.0
    """
    return sum(order_total(order) for order in orders)


def sum_totals(items):
    """Add type hints: items is an Iterable of anything HasTotal-shaped;
    result is float.

    Sum `.total()` across every item — works for `Cart`s, or anything
    else with a `total()` method, structurally.

    sum_totals([Cart([{"id": "1", "item": "Mug", "qty": 2, "price": 5.0}])])
        -> 10.0
    """
    return sum(item.total() for item in items)


class Cart:
    """Add type hints to `__init__` and `total`. A cart bundling a list
    of orders; satisfies `HasTotal` structurally (no inheritance).

    Cart([{"id": "1", "item": "Mug", "qty": 2, "price": 5.0}]).total() -> 10.0
    """

    def __init__(self, orders):
        self.orders = orders

    def total(self):
        return total_revenue(self.orders)
