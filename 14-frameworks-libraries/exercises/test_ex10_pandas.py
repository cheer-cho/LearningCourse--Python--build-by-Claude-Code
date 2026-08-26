import pytest

pytest.importorskip("pandas")

from ex10_pandas import add_margin_column, revenue_by_region, to_frame, top_products

RECORDS = [
    {"product": "Widget", "region": "East", "revenue": 100.0, "cost": 60.0},
    {"product": "Gadget", "region": "East", "revenue": 50.0, "cost": 20.0},
    {"product": "Widget", "region": "West", "revenue": 200.0, "cost": 90.0},
    {"product": "Gizmo", "region": "West", "revenue": 30.0, "cost": 10.0},
]


def test_to_frame_builds_expected_shape():
    df = to_frame(RECORDS)
    assert list(df.columns) == ["product", "region", "revenue", "cost"]
    assert len(df) == 4


def test_revenue_by_region_sums_per_group():
    df = to_frame(RECORDS)
    assert revenue_by_region(df) == {"East": 150.0, "West": 230.0}


def test_add_margin_column_computes_revenue_minus_cost():
    df = to_frame(RECORDS)
    result = add_margin_column(df)
    assert result["margin"].tolist() == [40.0, 30.0, 110.0, 20.0]


def test_add_margin_column_does_not_mutate_input():
    df = to_frame(RECORDS)
    add_margin_column(df)
    assert "margin" not in df.columns


def test_top_products_returns_highest_revenue_first():
    df = to_frame(RECORDS)
    result = top_products(df, 2)
    assert result["product"].tolist() == ["Widget", "Widget"]
    assert result["revenue"].tolist() == [200.0, 100.0]


def test_top_products_has_fresh_index():
    df = to_frame(RECORDS)
    result = top_products(df, 2)
    assert result.index.tolist() == [0, 1]
