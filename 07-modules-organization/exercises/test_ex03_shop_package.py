from mod07_shop import cart_total, discounted


def test_discounted_applies_percent_off():
    assert discounted(100, 25) == 75.0


def test_discounted_zero_percent_off():
    assert discounted(50, 0) == 50.0


def test_discounted_rounds_to_two_decimals():
    assert discounted(10, 33) == 6.7


def test_cart_total_sums_discounted_items():
    assert cart_total([100, 50], 10) == 135.0


def test_cart_total_no_discount():
    assert cart_total([10, 20, 30], 0) == 60.0


def test_cart_total_empty_cart_is_zero():
    assert cart_total([], 20) == 0.0
