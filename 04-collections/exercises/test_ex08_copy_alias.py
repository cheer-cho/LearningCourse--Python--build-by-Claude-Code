from ex08_copy_alias import broken_reset, deep_trap, independent_deep_copy, safe_flat_copy


def test_broken_reset_returns_equal_list():
    assert broken_reset([1, 2, 3]) == [1, 2, 3]


def test_broken_reset_is_not_an_alias():
    original = [1, 2, 3]
    result = broken_reset(original)
    result.append(4)
    assert original == [1, 2, 3]


def test_deep_trap_returns_equal_board():
    assert deep_trap([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]


def test_deep_trap_rows_are_independent():
    board = [[1, 2], [3, 4]]
    result = deep_trap(board)
    result[0].append(99)
    assert board == [[1, 2], [3, 4]]


def test_safe_flat_copy_appends_extra():
    assert safe_flat_copy([1, 2, 3], 4) == [1, 2, 3, 4]


def test_safe_flat_copy_does_not_mutate_base():
    base = [1, 2, 3]
    safe_flat_copy(base, 4)
    assert base == [1, 2, 3]


def test_independent_deep_copy_appends_to_correct_row():
    board = [[1, 2], [3, 4]]
    result = independent_deep_copy(board, 0, 99)
    assert result == [[1, 2, 99], [3, 4]]


def test_independent_deep_copy_does_not_mutate_original_board():
    board = [[1, 2], [3, 4]]
    independent_deep_copy(board, 0, 99)
    assert board == [[1, 2], [3, 4]]
