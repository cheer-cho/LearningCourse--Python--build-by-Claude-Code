from ex12_peekable import Peekable


def test_peek_shows_next_value_without_consuming():
    p = Peekable([1, 2, 3])
    assert p.peek() == 1
    assert p.peek() == 1  # peeking again doesn't advance
    assert next(p) == 1


def test_next_after_peek_returns_the_peeked_value():
    p = Peekable([1, 2, 3])
    p.peek()
    assert next(p) == 1
    assert next(p) == 2


def test_iterating_yields_remaining_values_after_a_peek():
    p = Peekable([1, 2, 3])
    p.peek()
    assert list(p) == [1, 2, 3]


def test_peek_on_empty_returns_none_by_default():
    assert Peekable([]).peek() is None


def test_peek_on_empty_returns_the_given_default():
    assert Peekable([]).peek("done") == "done"


def test_next_on_exhausted_raises_stop_iteration():
    p = Peekable([])
    try:
        next(p)
    except StopIteration:
        pass
    else:
        raise AssertionError("expected StopIteration")


def test_works_over_any_iterable_not_just_lists():
    p = Peekable(x * x for x in range(3))
    assert p.peek() == 0
    assert list(p) == [0, 1, 4]


def test_peekable_is_its_own_iterator():
    p = Peekable([1, 2])
    assert iter(p) is p


def test_works_in_a_for_loop():
    p = Peekable([1, 2, 3])
    seen = [value for value in p]
    assert seen == [1, 2, 3]
