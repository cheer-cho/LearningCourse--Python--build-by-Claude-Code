# Scenario: a bank-account withdrawal that reports exactly how short the
# balance was. Concepts: defining a custom exception class with its own
# `__init__`, storing extra attributes on it, raising it.
# Run: uv run pytest 06-errors-files -k ex04


class InsufficientFunds(Exception):
    """Raised when a withdrawal would overdraw an account.

    Carries `needed` (the amount requested) and `available` (the
    current balance) as attributes, so calling code can inspect the
    shortfall without parsing the message string.
    """

    def __init__(self, needed, available):
        super().__init__(f"need {needed}, only have {available}")
        self.needed = needed
        self.available = available


def withdraw(balance, amount):
    """Return `balance - amount` if `amount` can be covered by `balance`.

    Otherwise raise InsufficientFunds(needed=amount, available=balance)
    without changing anything (there's nothing to mutate — `balance` is
    just a number).

    withdraw(100, 30) -> 70
    withdraw(100, 150) -> raises InsufficientFunds with .needed == 150
                           and .available == 100
    """
    raise NotImplementedError
