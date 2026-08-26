from ex07_decorators import count_calls, log_calls


def test_log_calls_records_a_call():
    log = []

    @log_calls(log)
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    assert log == ["add(2, 3) -> 5"]


def test_log_calls_records_every_call_in_order():
    log = []

    @log_calls(log)
    def shout(word):
        return word.upper()

    shout("hi")
    shout("bye")
    assert log == ['shout(\'hi\') -> \'HI\'', "shout('bye') -> 'BYE'"]


def test_log_calls_preserves_metadata():
    log = []

    @log_calls(log)
    def add(a, b):
        """Add two numbers."""
        return a + b

    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."


def test_count_calls_starts_at_zero():
    @count_calls
    def ping():
        return "pong"

    assert ping.calls == 0


def test_count_calls_increments_on_each_call():
    @count_calls
    def ping():
        return "pong"

    ping()
    ping()
    ping()
    assert ping.calls == 3


def test_count_calls_returns_the_original_result():
    @count_calls
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_count_calls_preserves_metadata():
    @count_calls
    def ping():
        """Returns pong."""
        return "pong"

    assert ping.__name__ == "ping"
    assert ping.__doc__ == "Returns pong."
