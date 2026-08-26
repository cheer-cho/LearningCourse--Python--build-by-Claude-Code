from ex02_tuples_unpacking import distance, head_tail, min_max


def test_min_max_typical():
    assert min_max([3, 1, 4, 1, 5]) == (1, 5)


def test_min_max_single_item():
    assert min_max([7]) == (7, 7)


def test_min_max_all_same():
    assert min_max([2, 2, 2]) == (2, 2)


def test_head_tail_multiple_items():
    assert head_tail([1, 2, 3]) == (1, [2, 3])


def test_head_tail_single_item():
    assert head_tail([9]) == (9, [])


def test_distance_3_4_5_triangle():
    assert distance((0, 0), (3, 4)) == 5.0


def test_distance_same_point_is_zero():
    assert distance((1, 1), (1, 1)) == 0.0


def test_distance_negative_coordinates():
    assert distance((-1, -1), (2, 3)) == 5.0
