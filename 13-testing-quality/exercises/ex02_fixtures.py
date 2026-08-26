# Scenario: a bank-account test suite needs fresh accounts and a fake
# clock instead of the real one. Concepts: factory functions as
# fixtures, isolated state per instance, the "fake" test double.
# Run: uv run pytest 13-testing-quality -k ex02

import itertools
from dataclasses import dataclass

_account_ids = itertools.count(1)


@dataclass
class Account:
    """A bank account. Given — not part of the exercise."""

    id: int
    balance: float


def fresh_account() -> Account:
    """Return a new `Account` with balance 0.0 and an id that has never
    been used by a previous call to `fresh_account`/`funded_account` in
    this process (use `_account_ids`, defined above, to get it).

    a = fresh_account()
    b = fresh_account()
    a.id != b.id  -> True
    a.balance -> 0.0
    """
    raise NotImplementedError


def funded_account(balance: float) -> Account:
    """Like `fresh_account`, but starting with `balance` instead of 0.0.
    Must also get a unique id from `_account_ids`.

    funded_account(100.0) -> Account(id=<unique>, balance=100.0)
    """
    raise NotImplementedError


class FakeClock:
    """A test double standing in for the real clock. Given — not part
    of the exercise. `fake_clock` below is what you implement.
    """

    def __init__(self, start: float) -> None:
        self._seconds = start

    def now(self) -> float:
        return self._seconds

    def advance(self, secs: float) -> None:
        self._seconds += secs


def fake_clock(start: float = 0.0) -> FakeClock:
    """Return a fresh `FakeClock` starting at `start`. Every call must
    return an independent clock — advancing one returned clock must
    never affect any other clock this function has returned.

    c1 = fake_clock(100.0)
    c2 = fake_clock(100.0)
    c1.advance(5)
    c1.now() -> 105.0
    c2.now() -> 100.0   # untouched
    """
    raise NotImplementedError
