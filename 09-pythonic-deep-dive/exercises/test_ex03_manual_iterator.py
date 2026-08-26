from ex03_manual_iterator import Countdown


def test_list_counts_down_to_one():
    assert list(Countdown(3)) == [3, 2, 1]


def test_zero_start_yields_nothing():
    assert list(Countdown(0)) == []


def test_iterating_twice_gives_the_same_result_both_times():
    countdown = Countdown(3)
    assert list(countdown) == [3, 2, 1]
    assert list(countdown) == [3, 2, 1]


def test_iter_returns_a_fresh_iterator_object_each_time():
    countdown = Countdown(2)
    first = iter(countdown)
    second = iter(countdown)
    assert first is not second


def test_iterator_is_its_own_iterable():
    it = iter(Countdown(2))
    assert iter(it) is it


def test_manual_next_calls_raise_stop_iteration_when_exhausted():
    it = iter(Countdown(1))
    assert next(it) == 1
    try:
        next(it)
    except StopIteration:
        pass
    else:
        raise AssertionError("expected StopIteration")


def test_for_loop_works_via_the_protocol():
    seen = list(Countdown(3))
    assert seen == [3, 2, 1]
