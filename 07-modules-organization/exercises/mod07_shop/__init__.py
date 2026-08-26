"""mod07_shop package — public API.

Re-exports `discounted` and `cart_total` so callers write
`from mod07_shop import discounted, cart_total` without knowing which
submodule they live in. This file and its siblings (`pricing.py`,
`cart.py`) are thin, GIVEN wiring — edit the _impl files, not the
package files: `mod07_shop_pricing_impl.py` and
`mod07_shop_cart_impl.py`, both flat in `exercises/`.
"""

from mod07_shop.cart import cart_total
from mod07_shop.pricing import discounted

__all__ = ["cart_total", "discounted"]
