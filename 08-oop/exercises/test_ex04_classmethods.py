from ex04_classmethods import Pizza


def test_margherita_toppings():
    assert Pizza.margherita().toppings == ["tomato", "cheese", "basil"]


def test_hawaiian_toppings():
    assert Pizza.hawaiian().toppings == ["ham", "pineapple", "cheese"]


def test_margherita_and_hawaiian_are_independent_instances():
    m = Pizza.margherita()
    h = Pizza.hawaiian()
    assert m.toppings != h.toppings


def test_from_string_splits_on_comma():
    assert Pizza.from_string("pepperoni,olives").toppings == ["pepperoni", "olives"]


def test_from_string_strips_whitespace():
    assert Pizza.from_string("ham, pineapple").toppings == ["ham", "pineapple"]


def test_from_string_single_topping():
    assert Pizza.from_string("cheese").toppings == ["cheese"]


def test_from_string_drops_trailing_empty_piece():
    assert Pizza.from_string("cheese,").toppings == ["cheese"]


def test_valid_topping_true_for_known_topping():
    assert Pizza.valid_topping("cheese") is True


def test_valid_topping_case_insensitive():
    assert Pizza.valid_topping("Cheese") is True


def test_valid_topping_false_for_unknown_topping():
    assert Pizza.valid_topping("anchovy") is False
