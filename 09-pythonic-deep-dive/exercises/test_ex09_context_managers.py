import pytest
from ex09_context_managers import Stopwatch, ledger_transaction


class _Boom(Exception):
    """Marker exception for tests. Deliberately NOT RuntimeError, since
    NotImplementedError (raised by an unsolved stub) IS a RuntimeError
    subclass and would otherwise let a broken stub pass by accident."""


def test_stopwatch_records_elapsed_time():
    readings = iter([10.0, 12.5])
    with Stopwatch(lambda: next(readings)) as sw:
        pass
    assert sw.elapsed == 2.5


def test_stopwatch_returns_self_from_enter():
    readings = iter([0.0, 1.0])
    watch = Stopwatch(lambda: next(readings))
    with watch as sw:
        assert sw is watch


def test_stopwatch_does_not_swallow_exceptions():
    readings = iter([0.0, 1.0])
    watch = Stopwatch(lambda: next(readings))
    with pytest.raises(_Boom), watch:
        raise _Boom("boom")


def test_stopwatch_still_records_elapsed_time_on_exception():
    readings = iter([0.0, 5.0])
    watch = Stopwatch(lambda: next(readings))
    with pytest.raises(_Boom), watch:
        raise _Boom("boom")
    assert watch.elapsed == 5.0


def test_ledger_transaction_keeps_entries_on_success():
    ledger = []
    with ledger_transaction(ledger) as tx:
        tx.append(("deposit", 10))
    assert ledger == [("deposit", 10)]


def test_ledger_transaction_rolls_back_on_exception():
    ledger = []
    with pytest.raises(_Boom), ledger_transaction(ledger) as tx:
        tx.append(("deposit", 10))
        raise _Boom("boom")
    assert ledger == []


def test_ledger_transaction_only_rolls_back_its_own_entries():
    ledger = [("opening", 100)]
    with pytest.raises(_Boom), ledger_transaction(ledger) as tx:
        tx.append(("deposit", 10))
        raise _Boom("boom")
    assert ledger == [("opening", 100)]


def test_ledger_transaction_reraises_the_original_exception_type():
    ledger = []
    with pytest.raises(ValueError), ledger_transaction(ledger) as tx:
        tx.append(("withdraw", 5))
        raise ValueError("insufficient funds")
