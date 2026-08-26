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
        self.clock = clock
        self.elapsed = None
        self._start = None

    def __enter__(self):
        self._start = self.clock()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = self.clock() - self._start
        return False  # never swallow exceptions


@contextlib.contextmanager
def ledger_transaction(ledger):
    """Generator-based context manager (one yield = @contextmanager's
    whole trick). Yields `ledger` itself so the caller can append
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
    checkpoint = len(ledger)
    try:
        yield ledger
    except Exception:
        del ledger[checkpoint:]
        raise
