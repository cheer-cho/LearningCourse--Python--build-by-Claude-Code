from ex08_recursion import count_down_up, flatten, sum_digits


def test_sum_digits_multi_digit():
    assert sum_digits(1234) == 10


def test_sum_digits_single_digit():
    assert sum_digits(7) == 7


def test_sum_digits_zero():
    assert sum_digits(0) == 0


def test_flatten_nested_lists():
    assert flatten([1, [2, 3, [4], []], 5]) == [1, 2, 3, 4, 5]


def test_flatten_already_flat_list_unchanged():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_flatten_deeply_nested():
    assert flatten([[[[1]]], 2]) == [1, 2]


def test_flatten_empty_list():
    assert flatten([]) == []


def test_count_down_up_base_case():
    assert count_down_up(1) == "1 1"


def test_count_down_up_typical():
    assert count_down_up(3) == "3 2 1 1 2 3"


def test_count_down_up_larger():
    assert count_down_up(4) == "4 3 2 1 1 2 3 4"
