from ex04_for_range import factorial, stripes, sum_multiples


def test_sum_multiples_of_three_below_ten():
    assert sum_multiples(10, 3) == 18


def test_sum_multiples_of_five_below_twenty():
    assert sum_multiples(20, 5) == 30


def test_sum_multiples_none_below_limit():
    assert sum_multiples(5, 10) == 0


def test_sum_multiples_excludes_limit_itself():
    assert sum_multiples(9, 3) == 3 + 6


def test_factorial_zero_is_one():
    assert factorial(0) == 1


def test_factorial_five():
    assert factorial(5) == 120


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_guards_negative():
    assert factorial(-1) is None


def test_stripes_odd_length():
    assert stripes(5) == "=-=-="


def test_stripes_single_char():
    assert stripes(1) == "="


def test_stripes_empty():
    assert stripes(0) == ""


def test_stripes_even_length():
    assert stripes(4) == "=-=-"
