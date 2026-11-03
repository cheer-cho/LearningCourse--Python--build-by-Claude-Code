"""Checkpoint 02 — Receipt formatter.

Combines everything from this module: numbers, string methods,
f-string alignment/formatting, and tuple unpacking (no loops needed —
every receipt has exactly 3 items, so unpack them directly).

Passing `uv run python scripts/test.py 2` (or `uv run pytest
02-values-variables`) completes this module.
"""

from __future__ import annotations


def parse_money(text: str) -> float:
    """Parse a dollar-formatted price string into a float.

    Strip whitespace and a leading "$", then convert to float.

    parse_money("$12.30") -> 12.3
    parse_money(" $3.50 ") -> 3.5
    parse_money("9.99") -> 9.99
    """
    return float(text.strip().removeprefix("$"))


def format_receipt(store: str, items: list[tuple[str, str, int]]) -> str:
    """Build an aligned, multi-line receipt for exactly 3 items.

    `items` is a list of exactly 3 (name, unit_price_text, qty) tuples,
    e.g. [("Widget", "$3.50", 2), ...]. Unpack them directly — no loop
    needed: `a, b, c = items`. Parse each unit_price_text with
    `parse_money`. Apply a flat 7% tax.

    Layout (lines joined with "\\n"):
      1. "=== {store} ==="
      2-4. one line per item: `{name:<10} x{qty:<3} @ ${price:>6.2f} = ${line_total:>7.2f}`
      5. "-" * 34
      6. "{'Subtotal':<24}${subtotal:>8.2f}"
      7. "{'Tax (7%)':<24}${tax:>8.2f}"
      8. "{'Total':<24}${total:>8.2f}"

    All money values (price, line_total, subtotal, tax, total) are
    plain floats, formatted with the specs shown above — no manual
    rounding needed, the format spec handles 2 decimals.

    format_receipt("Corner Store", [
        ("Widget", "$3.50", 2), ("Gadget", "$12.00", 1), ("Gizmo", "$0.99", 5),
    ]) -> (see test_checkpoint_02.py for the exact expected lines)
    """
    
    #  1. get each item's values
    (item1_name, item1_unit_price_text, item1_qty) = items[0]
    (item2_name, item2_unit_price_text, item2_qty) = items[1]
    (item3_name, item3_unit_price_text, item3_qty) = items[2]

    # 2. parse price string to float
    item1_price = parse_money(item1_unit_price_text)
    item2_price = parse_money(item2_unit_price_text)
    item3_price = parse_money(item3_unit_price_text)

    # 3. get the line total value 
    item1_total_amount = item1_price * item1_qty
    item2_total_amount = item2_price * item2_qty
    item3_total_amount = item3_price * item3_qty

    subtotal = item1_total_amount + item2_total_amount + item3_total_amount
    tax = 0.07 * subtotal
    total = subtotal + tax

    line1 = f"{item1_name:<10} x{item1_qty:<3} @ ${item1_price:>6.2f} = ${item1_total_amount:>7.2f}"
    line2 = f"{item2_name:<10} x{item2_qty:<3} @ ${item2_price:>6.2f} = ${item2_total_amount:>7.2f}"
    line3 = f"{item3_name:<10} x{item3_qty:<3} @ ${item3_price:>6.2f} = ${item3_total_amount:>7.2f}"

    return "\n".join(
        [
            f"=== {store} ===",
            line1,
            line2,
            line3,
            "-" * 34,
            f"{'Subtotal':<24}${subtotal:>8.2f}",
            f"{'Tax (7%)':<24}${tax:>8.2f}",
            f"{'Total':<24}${total:>8.2f}",
        ]
    )

