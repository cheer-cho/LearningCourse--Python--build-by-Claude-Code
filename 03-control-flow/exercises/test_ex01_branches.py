from ex01_branches import grade, shipping_cost


def test_grade_a_at_boundary():
    assert grade(90) == "A"


def test_grade_a_above_boundary():
    assert grade(97) == "A"


def test_grade_b_range():
    assert grade(85) == "B"


def test_grade_c_range():
    assert grade(75) == "C"


def test_grade_d_range():
    assert grade(65) == "D"


def test_grade_f_below_sixty():
    assert grade(59) == "F"


def test_grade_f_well_below():
    assert grade(0) == "F"


def test_shipping_free_standard_at_threshold():
    assert shipping_cost(50, False) == 0.0


def test_shipping_free_standard_above_threshold():
    assert shipping_cost(75, False) == 0.0


def test_shipping_express_discounted_at_threshold():
    assert shipping_cost(60, True) == 4.99


def test_shipping_standard_fee_below_threshold():
    assert shipping_cost(20, False) == 5.99


def test_shipping_express_fee_below_threshold():
    assert shipping_cost(20, True) == 14.99
