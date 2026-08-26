# Scenario: a stopwatch and a rollback-on-error ledger transaction.
# Covers class-based context managers (__enter__/__exit__) and
# generator-based ones (@contextlib.contextmanager, one yield).
# Run: uv run pytest 09-pythonic-deep-dive -k ex09

import contextlib


class Stopwatch:
    """Class-based context manager that measures elapsed time using an
    injected `clock` callable (so tests are deterministic — no real
    time.time() needed). `__enter__` records the start reading and
    returns `self`; `__exit__` records `elapsed = end - start`.

    readings = iter([10.0, 12.5])
    with Stopwatch(lambda: next(readings)) as s:
        pass
    s.elapsed -> 2.5
    """

    def __init__(self, clock):
        raise NotImplementedError

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_value, traceback):
        """Record elapsed time and return False so exceptions still
        propagate — a Stopwatch never swallows errors."""
        raise NotImplementedError


@contextlib.contextmanager
def ledger_transaction(ledger):
    """Generator-based context manager (one yield = @contextmanager's
    whole trick). Yield `ledger` itself so the caller can append
    entries inside the `with` block. On success, the entries stay. On
    an exception inside the block, roll back every entry the block
    added, then let the exception propagate.

    ledger = []
    with ledger_transaction(ledger) as tx:
        tx.append(("deposit", 10))
    ledger -> [("deposit", 10)]

    ledger = []
    try:
        with ledger_transaction(ledger) as tx:
            tx.append(("deposit", 10))
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    ledger -> []   # rolled back
    """
    raise NotImplementedError
    yield  # pragma: no cover - marks this def as a generator for linters
