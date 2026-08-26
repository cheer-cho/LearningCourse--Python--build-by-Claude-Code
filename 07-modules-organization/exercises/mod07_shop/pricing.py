"""Thin wiring only — edit `mod07_shop_pricing_impl.py` (flat, in
exercises/), not this file. `scripts/verify_solutions.py` can only
overlay flat `solutions/*.py` files onto flat exercise files, so it
can't reach anything nested inside this package — the real logic has
to live in the flat _impl module instead.
"""

from mod07_shop_pricing_impl import discounted

__all__ = ["discounted"]
