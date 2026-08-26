import inspect

from drill01_loops import elementwise_diff, first_index_of, numbered_lines, pair_up

REWRITTEN = [pair_up, numbered_lines, elementwise_diff, first_index_of]


def test_pair_up_zips_names_and_scores():
    assert pair_up(["Ada", "Bo"], [90, 70]) == [("Ada", 90), ("Bo", 70)]


def test_pair_up_empty():
    assert pair_up([], []) == []


def test_numbered_lines_starts_at_one():
    assert numbered_lines(["a", "b"]) == ["1: a", "2: b"]


def test_numbered_lines_empty():
    assert numbered_lines([]) == []


def test_elementwise_diff_typical():
    assert elementwise_diff([10, 20, 30], [1, 25, 30]) == [9, 5, 0]


def test_elementwise_diff_empty():
    assert elementwise_diff([], []) == []


def test_first_index_of_found():
    assert first_index_of(["a", "b", "c"], "c") == 2


def test_first_index_of_missing():
    assert first_index_of(["a", "b"], "z") == -1


def test_rewrites_avoid_range_len_indexing():
    for func in REWRITTEN:
        source = inspect.getsource(func)
        assert "range(len" not in source, f"{func.__name__} still uses range(len(...))"
