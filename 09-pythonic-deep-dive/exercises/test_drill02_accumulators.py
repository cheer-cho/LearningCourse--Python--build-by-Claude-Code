import inspect

from drill02_accumulators import all_even, cart_total, has_failing_score, top_student

REWRITTEN = [cart_total, has_failing_score, all_even, top_student]


def test_cart_total_typical():
    cart = [{"price": 2.0, "quantity": 3}, {"price": 5.0, "quantity": 1}]
    assert cart_total(cart) == 11.0


def test_cart_total_empty():
    assert cart_total([]) == 0


def test_has_failing_score_true_when_one_is_below():
    assert has_failing_score([90, 55, 88], 60) is True


def test_has_failing_score_false_when_all_pass():
    assert has_failing_score([90, 95], 60) is False


def test_has_failing_score_empty_is_false():
    assert has_failing_score([], 60) is False


def test_all_even_true_for_all_even():
    assert all_even([2, 4, 6]) is True


def test_all_even_false_with_one_odd():
    assert all_even([2, 3, 4]) is False


def test_all_even_empty_is_true():
    assert all_even([]) is True


def test_top_student_picks_highest_score():
    students = [{"name": "Ada", "score": 91}, {"name": "Bo", "score": 88}]
    assert top_student(students) == "Ada"


def test_rewrites_avoid_append():
    for func in REWRITTEN:
        source = inspect.getsource(func)
        assert ".append" not in source, f"{func.__name__} still builds a list with .append"
