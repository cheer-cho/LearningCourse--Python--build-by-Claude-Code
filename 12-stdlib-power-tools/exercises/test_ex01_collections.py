from ex01_collections import LastN, group_by_first_letter, top_words


def test_top_words_ranks_by_count_descending():
    assert top_words("a b b c c c", 2) == [("c", 3), ("b", 2)]


def test_top_words_ties_break_alphabetically():
    assert top_words("x x y y", 2) == [("x", 2), ("y", 2)]


def test_top_words_n_larger_than_distinct_words():
    assert top_words("a a b", 5) == [("a", 2), ("b", 1)]


def test_top_words_empty_text():
    assert top_words("", 3) == []


def test_group_by_first_letter_groups_and_preserves_order():
    names = ["Ada", "Al", "Bo", "Amy"]
    assert group_by_first_letter(names) == {"A": ["Ada", "Al", "Amy"], "B": ["Bo"]}


def test_group_by_first_letter_empty_list():
    assert group_by_first_letter([]) == {}


def test_group_by_first_letter_single_name():
    assert group_by_first_letter(["Zed"]) == {"Z": ["Zed"]}


def test_lastn_keeps_only_most_recent():
    keeper = LastN(2)
    keeper.add(1)
    keeper.add(2)
    keeper.add(3)
    assert keeper.items() == [2, 3]


def test_lastn_empty_before_any_add():
    keeper = LastN(3)
    assert keeper.items() == []


def test_lastn_under_capacity_keeps_everything():
    keeper = LastN(5)
    keeper.add("a")
    keeper.add("b")
    assert keeper.items() == ["a", "b"]
