import pytest
from ex04_custom_exceptions import InsufficientFunds, withdraw


def test_withdraw_returns_new_balance_when_covered():
    assert withdraw(100, 30) == 70


def test_withdraw_exact_balance_is_allowed():
    assert withdraw(50, 50) == 0


def test_withdraw_raises_insufficient_funds_when_short():
    with pytest.raises(InsufficientFunds):
        withdraw(100, 150)


def test_withdraw_error_carries_needed_and_available():
    with pytest.raises(InsufficientFunds) as excinfo:
        withdraw(100, 150)
    assert excinfo.value.needed == 150
    assert excinfo.value.available == 100


def test_withdraw_error_message_mentions_both_numbers():
    with pytest.raises(InsufficientFunds, match="need 150, only have 100"):
        withdraw(100, 150)
