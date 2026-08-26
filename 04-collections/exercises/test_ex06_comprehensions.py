from ex06_comprehensions import celsius_table, first_letters, name_lengths, squares_of_evens


def test_squares_of_evens_typical():
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]


def test_squares_of_evens_no_evens():
    assert squares_of_evens([1, 3, 5]) == []


def test_squares_of_evens_preserves_order():
    assert squares_of_evens([4, 2, 6]) == [16, 4, 36]


def test_name_lengths_typical():
    assert name_lengths(["Ada", "Grace"]) == {"Ada": 3, "Grace": 5}


def test_name_lengths_empty_list():
    assert name_lengths([]) == {}


def test_first_letters_dedupes():
    assert first_letters(["cat", "car", "dog"]) == {"c", "d"}


def test_first_letters_skips_empty_strings():
    assert first_letters(["cat", ""]) == {"c"}


def test_celsius_table_typical():
    assert celsius_table(0, 2) == {0: 32.0, 1: 33.8}


def test_celsius_table_empty_range():
    assert celsius_table(5, 5) == {}
