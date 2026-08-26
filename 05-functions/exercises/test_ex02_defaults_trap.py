from ex02_defaults_trap import add_item, power


def test_power_default_exponent_squares():
    assert power(3) == 9


def test_power_explicit_exponent():
    assert power(2, 5) == 32


def test_power_zero_exponent_is_one():
    assert power(7, 0) == 1


def test_add_item_returns_list_with_item():
    assert add_item(1) == [1]


def test_add_item_appends_to_provided_list():
    assert add_item(2, [1]) == [1, 2]


def test_add_item_default_is_independent_across_calls():
    first = add_item("a")
    second = add_item("b")
    assert first == ["a"]
    assert second == ["b"]


def test_add_item_called_three_times_stays_independent():
    results = [add_item("x") for _ in range(3)]
    assert results == [["x"], ["x"], ["x"]]
