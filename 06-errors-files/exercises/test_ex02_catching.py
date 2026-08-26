import pytest
from ex02_catching import first_working, int_or_default, safe_divide


def test_safe_divide_normal_case():
    assert safe_divide(10, 2) == 5.0


def test_safe_divide_returns_none_on_zero_division():
    assert safe_divide(10, 0) is None


def test_int_or_default_parses_valid_int():
    assert int_or_default("42", 0) == 42


def test_int_or_default_returns_default_on_bad_text():
    assert int_or_default("nope", 0) == 0


def test_int_or_default_returns_default_on_empty_string():
    assert int_or_default("", -1) == -1


def test_first_working_returns_first_success():
    assert first_working([lambda: 1 / 0, lambda: 7]) == 7


def test_first_working_skips_multiple_failures():
    calls = []

    def ok():
        calls.append("ok")
        return "done"

    assert first_working([lambda: 1 / 0, lambda: int("x"), ok]) == "done"
    assert calls == ["ok"]


def test_first_working_raises_last_exception_when_all_fail():
    with pytest.raises(ZeroDivisionError):
        first_working([lambda: int("x"), lambda: 1 / 0])
