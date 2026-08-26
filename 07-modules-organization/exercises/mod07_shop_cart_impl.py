# Scenario: cart totals for the tiny shop package `mod07_shop/`. This
# file backs `mod07_shop/cart.py` — edit HERE, not the package file
# (same "_impl" reason as `mod07_shop_pricing_impl.py`). Concepts:
# importing one flat _impl module from another.
# Run: uv run pytest 07-modules-organization -k ex03

from mod07_shop_pricing_impl import discounted  # noqa: F401 — needed once cart_total is implemented


def cart_total(prices, percent_off=0):
    """Return the total cost of `prices` (a list of item prices) after
    applying `percent_off` to each item, rounded to 2 decimal places.

    Reuse `discounted` for the per-item math — don't recompute the
    percentage yourself.

    cart_total([100, 50], 10) -> 135.0
    cart_total([10, 20, 30], 0) -> 60.0
    cart_total([], 20) -> 0.0
    """
    raise NotImplementedError
