from __future__ import annotations

from ex03_fstrings import debug_pair, price_tag, progress_line


def test_price_tag_widget() -> None:
    assert price_tag("Widget", 3.5) == "Widget........$   3.50"


def test_price_tag_mug() -> None:
    assert price_tag("Mug", 12.0) == "Mug...........$  12.00"


def test_progress_line_partial() -> None:
    assert progress_line(7) == "Progress:   7.0%"


def test_progress_line_full() -> None:
    assert progress_line(100) == "Progress: 100.0%"


def test_debug_pair_int() -> None:
    assert debug_pair(5) == "x=5"


def test_debug_pair_string() -> None:
    assert debug_pair("hi") == "x='hi'"
