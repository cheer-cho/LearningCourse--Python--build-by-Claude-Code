import pytest
from checkpoint_05 import apply_all, make_formatter, word_stats


def test_word_stats_counts_words():
    assert word_stats("the cat sat on the mat") == {
        "the": 2,
        "cat": 1,
        "sat": 1,
        "on": 1,
        "mat": 1,
    }


def test_word_stats_filters_by_min_length():
    assert word_stats("a bb ccc", min_length=2) == {"bb": 1, "ccc": 1}


def test_word_stats_filters_stop_words():
    assert word_stats("the cat sat on the mat", stop_words={"the", "on"}) == {
        "cat": 1,
        "sat": 1,
        "mat": 1,
    }


def test_word_stats_strips_basic_punctuation():
    assert word_stats("Cat, cat! dog.") == {"cat": 2, "dog": 1}


def test_word_stats_default_stop_words_do_not_leak_across_calls():
    first = word_stats("the cat", stop_words={"the"})
    second = word_stats("the cat")
    assert first == {"cat": 1}
    assert second == {"the": 1, "cat": 1}


def test_word_stats_min_length_is_keyword_only():
    with pytest.raises(TypeError):
        word_stats("a bb ccc", 2)


def test_word_stats_stop_words_is_keyword_only():
    with pytest.raises(TypeError):
        word_stats("a bb ccc", 1, {"a"})


def test_make_formatter_wraps_value():
    bracket = make_formatter("[", "]")
    assert bracket("info") == "[info]"


def test_make_formatter_default_suffix_is_empty():
    shout = make_formatter(">> ")
    assert shout("hello") == ">> hello"


def test_make_formatter_instances_are_independent():
    bracket = make_formatter("[", "]")
    paren = make_formatter("(", ")")
    assert bracket("x") == "[x]"
    assert paren("x") == "(x)"


def test_apply_all_threads_left_to_right():
    assert apply_all(3, lambda x: x + 1, lambda x: x * 2) == 8


def test_apply_all_no_funcs_returns_value_unchanged():
    assert apply_all(5) == 5


def test_apply_all_single_func():
    assert apply_all(2, lambda x: x**2) == 4
