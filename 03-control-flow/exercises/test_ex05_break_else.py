from ex05_break_else import find_char, first_divisor, is_prime


def test_first_divisor_composite():
    assert first_divisor(12) == 2


def test_first_divisor_odd_composite():
    assert first_divisor(9) == 3


def test_first_divisor_prime_returns_itself():
    assert first_divisor(7) == 7


def test_first_divisor_guards_below_two():
    assert first_divisor(1) is None


def test_is_prime_true_for_seven():
    assert is_prime(7) is True


def test_is_prime_false_for_eight():
    assert is_prime(8) is False


def test_is_prime_false_for_one():
    assert is_prime(1) is False


def test_is_prime_true_for_two():
    assert is_prime(2) is True


def test_is_prime_false_for_nine():
    assert is_prime(9) is False


def test_find_char_present():
    assert find_char("hello", "l") == 2


def test_find_char_first_index():
    assert find_char("hello", "h") == 0


def test_find_char_absent():
    assert find_char("hello", "z") == -1


def test_find_char_empty_string():
    assert find_char("", "a") == -1
