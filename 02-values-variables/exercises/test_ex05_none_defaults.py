from __future__ import annotations

from ex05_none_defaults import first_non_none, label_or_default


def test_label_or_default_with_label() -> None:
    assert label_or_default("Ada") == "Ada"


def test_label_or_default_with_none() -> None:
    assert label_or_default(None) == "(none)"


def test_label_or_default_empty_string_is_kept() -> None:
    # "" is not None, so it should NOT be replaced with "(none)".
    assert label_or_default("") == ""


def test_first_non_none_returns_a() -> None:
    assert first_non_none("Ada", "Unknown") == "Ada"


def test_first_non_none_falls_back_to_b() -> None:
    assert first_non_none(None, "Unknown") == "Unknown"


def test_first_non_none_keeps_falsy_but_not_none_value() -> None:
    assert first_non_none(0, "Unknown") == 0
