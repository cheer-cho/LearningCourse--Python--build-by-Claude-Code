from ex06_closures import make_accumulator, make_button_handlers, make_multiplier


def test_make_multiplier_scales_by_k():
    triple = make_multiplier(3)
    assert triple(5) == 15
    assert triple(0) == 0


def test_make_multiplier_instances_are_independent():
    double = make_multiplier(2)
    triple = make_multiplier(3)
    assert double(4) == 8
    assert triple(4) == 12


def test_make_accumulator_running_total():
    acc = make_accumulator()
    assert acc(10) == 10
    assert acc(5) == 15
    assert acc(-3) == 12


def test_make_accumulator_instances_are_independent():
    a = make_accumulator()
    b = make_accumulator()
    a(100)
    assert b(1) == 1


def test_make_button_handlers_each_remembers_its_own_index():
    handlers = make_button_handlers(["Save", "Cancel", "Delete"])
    assert handlers[0]() == "Save clicked (button 0)"
    assert handlers[1]() == "Cancel clicked (button 1)"
    assert handlers[2]() == "Delete clicked (button 2)"


def test_make_button_handlers_survives_calling_out_of_order():
    handlers = make_button_handlers(["A", "B"])
    assert handlers[1]() == "B clicked (button 1)"
    assert handlers[0]() == "A clicked (button 0)"
