"""ex03 — f-strings: interpolation, number formatting, alignment.

Scenario: building small formatted lines of output, like a receipt
would need. Covers f-string basics, `:.2f`, alignment/fill specs, and
the `=` debug spec.

Check: uv run python scripts/test.py 2 -k ex03
"""

from __future__ import annotations


def price_tag(name: str, price: float) -> str:
    """Build a price-tag line: name, dot-filled, then a 2-decimal price.

    Format: name left-aligned and dot-filled to 14 characters, then
    "$ ", then the price right-aligned to width 6 with 2 decimals.
    Format spec hint: `{name:.<14}` and `{price:>6.2f}`.

    price_tag("Widget", 3.5) -> "Widget........$   3.50"
    price_tag("Mug", 12.0) -> "Mug...........$  12.00"
    """
    raise NotImplementedError


def progress_line(pct: float) -> str:
    """Build a one-line progress readout.

    Format: "Progress: " followed by the percentage right-aligned to
    width 5 with 1 decimal, then "%".

    progress_line(7) -> "Progress:   7.0%"
    progress_line(100) -> "Progress: 100.0%"
    """
    raise NotImplementedError


def debug_pair(x: object) -> str:
    """Show a value using the f-string debug spec `{x=}`.

    The `=` debug spec prints both the expression text and its repr —
    great for quick print-debugging.

    debug_pair(5) -> "x=5"
    debug_pair("hi") -> "x='hi'"
    """
    raise NotImplementedError
