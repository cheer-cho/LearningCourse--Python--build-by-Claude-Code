from __future__ import annotations

from ex04_bools import is_teen, same_object, same_value


def test_is_teen_lower_bound() -> None:
    assert is_teen(13) is True


def test_is_teen_upper_bound() -> None:
    assert is_teen(19) is True


def test_is_teen_too_old() -> None:
    assert is_teen(20) is False


def test_is_teen_too_young() -> None:
    assert is_teen(5) is False


def test_same_object_false_for_equal_but_distinct_lists() -> None:
    assert same_object([1, 2], [1, 2]) is False


def test_same_object_true_for_the_same_list() -> None:
    shared = [1, 2]
    assert same_object(shared, shared) is True


def test_same_value_true_for_equal_lists() -> None:
    assert same_value([1, 2], [1, 2]) is True


def test_same_value_false_for_different_lists() -> None:
    assert same_value([1, 2], [1, 2, 3]) is False
