"""Customer records for the tiny shop in ex06 — see `mod07_orders.py`
for the circular-import story this pair used to have and how it was
fixed (extracting the shared `format_money` into `ex06_circular_fix.py`).
"""

from ex06_circular_fix import format_money


def customer_balance_line(name, cents):
    """Return a one-line balance like "Ada owes $5.00"."""
    return f"{name} owes {format_money(cents)}"
