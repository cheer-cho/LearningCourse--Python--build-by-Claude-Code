from ex11_itertools import first_matching, group_by_grade, top_pairs, window


def test_top_pairs_caps_at_n():
    assert top_pairs([1, 2], ["x", "y"], 3) == [(1, "x"), (1, "y"), (2, "x")]


def test_top_pairs_never_exceeds_the_full_product():
    assert top_pairs([1], ["x"], 5) == [(1, "x")]


def test_top_pairs_zero_is_empty():
    assert top_pairs([1, 2], ["x"], 0) == []


def test_window_pairs_are_consecutive():
    assert list(window([1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4)]


def test_window_single_item_is_empty():
    assert list(window([1])) == []


def test_window_empty_is_empty():
    assert list(window([])) == []


def test_group_by_grade_groups_all_matching_students():
    students = [
        {"name": "Ada", "grade": "A"},
        {"name": "Bo", "grade": "B"},
        {"name": "Cy", "grade": "A"},
    ]
    assert group_by_grade(students) == {"A": ["Ada", "Cy"], "B": ["Bo"]}


def test_group_by_grade_handles_unsorted_input():
    students = [
        {"name": "Bo", "grade": "B"},
        {"name": "Ada", "grade": "A"},
    ]
    assert group_by_grade(students) == {"A": ["Ada"], "B": ["Bo"]}


def test_group_by_grade_empty_input():
    assert group_by_grade([]) == {}


def test_first_matching_returns_first_hit():
    assert first_matching([1, 3, 4, 7], lambda x: x % 2 == 0) == 4


def test_first_matching_returns_none_when_nothing_matches():
    assert first_matching([1, 3, 5], lambda x: x % 2 == 0) is None


def test_first_matching_stops_pulling_after_the_first_hit():
    pulled = []

    def spy():
        for n in [1, 3, 4, 7, 100]:
            pulled.append(n)
            yield n

    result = first_matching(spy(), lambda x: x % 2 == 0)
    assert result == 4
    assert pulled == [1, 3, 4]
