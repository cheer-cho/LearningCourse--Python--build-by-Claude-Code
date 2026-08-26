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
    raise NotImplementedError


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
    raise NotImplementedError
