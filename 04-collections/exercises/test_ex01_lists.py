from ex01_lists import insert_sorted, top_three, without_negatives


def test_top_three_picks_three_highest_descending():
    assert top_three([50, 90, 10, 100, 70]) == [100, 90, 70]


def test_top_three_does_not_mutate_input():
    scores = [50, 90, 10, 100, 70]
    top_three(scores)
    assert scores == [50, 90, 10, 100, 70]


def test_top_three_fewer_than_three_items():
    assert top_three([5, 1]) == [5, 1]


def test_top_three_empty_list():
    assert top_three([]) == []


def test_insert_sorted_middle():
    assert insert_sorted([1, 3, 5], 4) == [1, 3, 4, 5]


def test_insert_sorted_front():
    assert insert_sorted([1, 3, 5], 0) == [0, 1, 3, 5]


def test_insert_sorted_end():
    assert insert_sorted([1, 3, 5], 9) == [1, 3, 5, 9]


def test_insert_sorted_into_empty():
    assert insert_sorted([], 7) == [7]


def test_without_negatives_keeps_order():
    assert without_negatives([3, -1, 0, -5, 2]) == [3, 0, 2]


def test_without_negatives_all_negative():
    assert without_negatives([-1, -2]) == []


def test_without_negatives_does_not_mutate_input():
    nums = [3, -1, 0]
    without_negatives(nums)
    assert nums == [3, -1, 0]
