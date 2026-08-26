from __future__ import annotations

from ex08_swap_and_augment import apply_raise_and_bonus, evaluate, swap


def test_swap_numbers() -> None:
    assert swap(1, 2) == (2, 1)


def test_swap_strings() -> None:
    assert swap("x", "y") == ("y", "x")


def test_apply_raise_and_bonus_typical() -> None:
    assert apply_raise_and_bonus(50000.0, 2000.0, 500.0) == 52500.0


def test_apply_raise_and_bonus_no_raise() -> None:
    assert apply_raise_and_bonus(100.0, 0.0, 10.0) == 110.0


def test_evaluate_hits_target() -> None:
    assert evaluate() == 20
