import itertools
from dataclasses import dataclass

_account_ids = itertools.count(1)


@dataclass
class Account:
    id: int
    balance: float


def fresh_account() -> Account:
    return Account(id=next(_account_ids), balance=0.0)


def funded_account(balance: float) -> Account:
    return Account(id=next(_account_ids), balance=balance)


class FakeClock:
    def __init__(self, start: float) -> None:
        self._seconds = start

    def now(self) -> float:
        return self._seconds

    def advance(self, secs: float) -> None:
        self._seconds += secs


def fake_clock(start: float = 0.0) -> FakeClock:
    return FakeClock(start)
