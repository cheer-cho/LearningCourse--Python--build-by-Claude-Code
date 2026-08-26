from ex03_while import collatz_steps, countdown


def test_countdown_from_three():
    assert countdown(3) == "3-2-1-liftoff"


def test_countdown_from_one():
    assert countdown(1) == "1-liftoff"


def test_countdown_from_zero_skips_to_liftoff():
    assert countdown(0) == "liftoff"


def test_countdown_negative_skips_to_liftoff():
    assert countdown(-5) == "liftoff"


def test_countdown_larger_number():
    assert countdown(5) == "5-4-3-2-1-liftoff"


def test_collatz_steps_already_one():
    assert collatz_steps(1) == 0


def test_collatz_steps_six():
    assert collatz_steps(6) == 8


def test_collatz_steps_power_of_two():
    assert collatz_steps(16) == 4


def test_collatz_steps_guards_zero():
    assert collatz_steps(0) is None


def test_collatz_steps_guards_negative():
    assert collatz_steps(-3) is None
