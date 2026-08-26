import pytest
from checkpoint_13 import BRANCH_LABELS, BRANCHES_HIT, QUOTE_CASES, make_edge_order, shipping_quote


def _order_only(case: dict) -> dict:
    return {k: v for k, v in case.items() if k != "expected"}


@pytest.mark.parametrize(
    "case",
    QUOTE_CASES,
    ids=[f"case{i}" for i in range(len(QUOTE_CASES))],
)
def test_quote_case_matches_expected_total(case):
    assert shipping_quote(_order_only(case)) == pytest.approx(case["expected"])


def test_quote_cases_cover_every_branch():
    BRANCHES_HIT.clear()
    for case in QUOTE_CASES:
        shipping_quote(_order_only(case))
    shipping_quote(make_edge_order())
    assert BRANCHES_HIT == BRANCH_LABELS


def test_make_edge_order_has_the_required_shape():
    order = make_edge_order()
    for key in ("subtotal", "weight_kg", "international", "express", "fragile"):
        assert key in order


def test_make_edge_order_is_the_nastiest_combination():
    order = make_edge_order()
    assert order["weight_kg"] >= 5
    assert order["international"] is True
    assert order["express"] is True
    assert order["fragile"] is True
    # High enough it WOULD qualify for free shipping if it were domestic.
    assert order["subtotal"] >= 100


def test_make_edge_order_never_gets_free_shipping():
    # International orders double the base rate; free shipping only
    # ever applies to domestic orders, no matter how high the subtotal.
    order = make_edge_order()
    assert shipping_quote(order) > 0.0
