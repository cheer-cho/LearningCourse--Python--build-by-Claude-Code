import pytest
from ex01_raising import parse_age, require_positive


def test_require_positive_returns_value_when_positive():
    assert require_positive(5) == 5


def test_require_positive_raises_on_negative():
    with pytest.raises(ValueError, match="expected a positive number, got -3"):
        require_positive(-3)


def test_require_positive_raises_on_zero():
    with pytest.raises(ValueError, match="expected a positive number, got 0"):
        require_positive(0)


def test_parse_age_valid_string():
    assert parse_age("30") == 30


def test_parse_age_raises_on_non_numeric():
    with pytest.raises(ValueError, match="invalid age: 'abc'"):
        parse_age("abc")


def test_parse_age_raises_on_negative():
    with pytest.raises(ValueError, match="age cannot be negative: -5"):
        parse_age("-5")
