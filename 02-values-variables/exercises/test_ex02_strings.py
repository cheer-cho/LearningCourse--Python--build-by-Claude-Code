from __future__ import annotations

from ex02_strings import clean_username, initials, shout


def test_shout_uppercases_and_adds_bang() -> None:
    assert shout("watch out") == "WATCH OUT!"


def test_shout_single_word() -> None:
    assert shout("hello") == "HELLO!"


def test_initials_ada_lovelace() -> None:
    assert initials("ada lovelace") == "A.L."


def test_initials_grace_hopper() -> None:
    assert initials("grace hopper") == "G.H."


def test_clean_username_strips_and_lowercases() -> None:
    assert clean_username("  John Doe ") == "john_doe"


def test_clean_username_already_lower() -> None:
    assert clean_username("ADA") == "ada"


def test_clean_username_replaces_all_spaces() -> None:
    assert clean_username("a b c") == "a_b_c"
