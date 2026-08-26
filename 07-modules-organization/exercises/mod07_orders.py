"""Order records for the tiny shop in ex06.

STORY: `mod07_orders.py` and `mod07_customers.py` used to import each
other's money-formatting helper directly (`from mod07_customers import
format_money` here, and the mirror image there) and crashed with a
circular ImportError on startup — neither module could finish loading
before the other needed it. The fix is applied below: both files now
import `format_money` from the flat stub `ex06_circular_fix.py`
instead of from each other. That's the standard fix for a circular
import — extract the shared code into a third module.
"""

from ex06_circular_fix import format_money


def order_summary(order_id, cents):
    """Return a one-line summary like "order 42: $19.99"."""
    return f"order {order_id}: {format_money(cents)}"
