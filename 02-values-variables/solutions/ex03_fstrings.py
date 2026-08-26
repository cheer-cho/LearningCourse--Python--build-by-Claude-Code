"""Reference solution for ex03_fstrings. See exercises/ex03_fstrings.py."""

from __future__ import annotations


def price_tag(name: str, price: float) -> str:
    return f"{name:.<14}$ {price:>6.2f}"


def progress_line(pct: float) -> str:
    return f"Progress: {pct:>5.1f}%"


def debug_pair(x: object) -> str:
    return f"{x=}"
