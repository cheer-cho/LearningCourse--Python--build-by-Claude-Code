from ex03_else_finally import guarded_process


def test_guarded_process_success_returns_result():
    log = []
    result = guarded_process({"divisor": 4}, log)
    assert result == 25.0


def test_guarded_process_success_event_order():
    log = []
    guarded_process({"divisor": 4}, log)
    assert log == ["start", "ok", "cleanup"]


def test_guarded_process_zero_divisor_returns_none():
    log = []
    result = guarded_process({"divisor": 0}, log)
    assert result is None


def test_guarded_process_zero_divisor_event_order():
    log = []
    guarded_process({"divisor": 0}, log)
    assert log == ["start", "error", "cleanup"]


def test_guarded_process_missing_key_event_order():
    log = []
    result = guarded_process({}, log)
    assert result is None
    assert log == ["start", "error", "cleanup"]


def test_guarded_process_appends_to_existing_log():
    log = ["previous"]
    guarded_process({"divisor": 2}, log)
    assert log == ["previous", "start", "ok", "cleanup"]
