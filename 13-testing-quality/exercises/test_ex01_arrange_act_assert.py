from ex01_arrange_act_assert import Order, describe_failure, make_order, make_paid_order


def test_make_order_defaults():
    order = make_order()
    assert order == Order(id=1, item="widget", quantity=1, unit_price=9.99, paid=False)


def test_make_order_override_one_field_keeps_the_rest():
    order = make_order(quantity=3)
    assert order.quantity == 3
    assert order.item == "widget"
    assert order.paid is False


def test_make_order_override_several_fields():
    order = make_order(item="gadget", unit_price=5.0, paid=True)
    assert order.item == "gadget"
    assert order.unit_price == 5.0
    assert order.paid is True


def test_make_order_returns_fresh_object_each_call():
    a = make_order()
    b = make_order()
    assert a == b
    assert a is not b


def test_make_paid_order_is_paid_by_default():
    order = make_paid_order()
    assert order.paid is True


def test_make_paid_order_ignores_paid_override():
    order = make_paid_order(paid=False)
    assert order.paid is True


def test_make_paid_order_still_honors_other_overrides():
    order = make_paid_order(item="gizmo", quantity=2)
    assert order.item == "gizmo"
    assert order.quantity == 2
    assert order.paid is True


def test_describe_failure_mentions_both_values():
    message = describe_failure(5, 3)
    assert "5" in message
    assert "3" in message


def test_describe_failure_uses_expected_and_actual_language():
    message = describe_failure(5, 3).lower()
    assert "expected" in message
    assert "got" in message or "actual" in message


def test_describe_failure_uses_repr_not_just_str():
    message = describe_failure("a", "b")
    assert repr("a") in message
    assert repr("b") in message


def test_describe_failure_is_not_hardcoded():
    first = describe_failure(1, 2)
    second = describe_failure(10, 20)
    assert first != second
