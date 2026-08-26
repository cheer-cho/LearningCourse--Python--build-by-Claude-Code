from ex01_define_return import clamp, greet_missing_return, rectangle_info


def test_rectangle_info_typical():
    assert rectangle_info(3, 4) == (12, 14)


def test_rectangle_info_square():
    assert rectangle_info(5, 5) == (25, 20)


def test_clamp_within_range_unchanged():
    assert clamp(5, 0, 10) == 5


def test_clamp_below_range_returns_lo():
    assert clamp(-3, 0, 10) == 0


def test_clamp_above_range_returns_hi():
    assert clamp(99, 0, 10) == 10


def test_clamp_at_exact_boundaries():
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_greet_missing_return_gives_back_the_string():
    assert greet_missing_return("Ada") == "Hello, Ada!"


def test_greet_missing_return_is_not_none():
    assert greet_missing_return("Bo") is not None
