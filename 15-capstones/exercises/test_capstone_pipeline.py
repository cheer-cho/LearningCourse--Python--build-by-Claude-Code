"""Acceptance tests for Capstone B, driven by the committed fixture
`data/messy_sales.csv`: 22 well-formed orders (across North/South,
Jan/Feb 2024, with mixed date formats, region casing, and "$" prices),
4 exact duplicate rows, and 14 bad rows (one deliberate problem each).
Expected shapes/values below were derived by hand from that fixture —
see LESSON.md's Capstone B section for the full breakdown.
"""

from __future__ import annotations

from pathlib import Path

import pytest

pytest.importorskip("pandas")

from capstone_pipeline import (
    PipelineError,
    aggregate,
    clean,
    load_sales,
    report,
    run,
)

FIXTURE = Path(__file__).parent / "data" / "messy_sales.csv"

EXPECTED_ISSUES = [
    "S001: duplicate row",
    "S006: duplicate row",
    "S012: duplicate row",
    "S018: duplicate row",
    "S023: missing region",
    "S024: missing region",
    "S025: missing product",
    "S026: missing quantity",
    "S027: missing quantity",
    "S028: missing price",
    "S029: invalid quantity",
    "S030: invalid quantity",
    "S031: invalid date",
    "S032: invalid date",
    "S033: invalid price",
    "S034: invalid price",
    "S035: invalid quantity",
    "S036: invalid quantity",
]


# --- load_sales --------------------------------------------------------


def test_load_sales_reads_all_raw_rows():
    df = load_sales(FIXTURE)
    assert len(df) == 40
    assert list(df.columns) == ["order_id", "date", "region", "product", "quantity", "price"]


def test_load_sales_missing_file_raises_pipeline_error(tmp_path):
    with pytest.raises(PipelineError):
        load_sales(tmp_path / "does_not_exist.csv")


# --- clean --------------------------------------------------------------


def test_clean_drops_exactly_the_bad_and_duplicate_rows():
    df = load_sales(FIXTURE)
    clean_df, issues = clean(df)
    assert clean_df.shape == (22, 6)
    assert issues == EXPECTED_ISSUES


def test_clean_normalizes_region_casing():
    df = load_sales(FIXTURE)
    clean_df, _ = clean(df)
    assert set(clean_df["region"].unique()) == {"North", "South"}


def test_clean_coerces_quantity_and_price_to_numbers():
    df = load_sales(FIXTURE)
    clean_df, _ = clean(df)
    assert clean_df["quantity"].dtype.kind == "i"
    assert clean_df["price"].dtype.kind == "f"
    row = clean_df.loc[clean_df["order_id"] == "S004"].iloc[0]
    assert row["quantity"] == 4
    assert row["price"] == 10.0


def test_clean_parses_every_supported_date_format_to_the_same_month():
    df = load_sales(FIXTURE)
    clean_df, _ = clean(df)
    jan_ids = {"S001", "S002", "S003", "S004", "S005"}
    months = clean_df.loc[clean_df["order_id"].isin(jan_ids), "date"].dt.strftime("%Y-%m")
    assert set(months) == {"2024-01"}


def test_clean_on_already_clean_frame_reports_no_issues():
    df = load_sales(FIXTURE)
    clean_df, _ = clean(df)
    re_raw = clean_df.astype(str)
    re_raw["date"] = clean_df["date"].dt.strftime("%Y-%m-%d")
    clean_again, issues = clean(re_raw)
    assert issues == []
    assert len(clean_again) == len(clean_df)


# --- aggregate & report --------------------------------------------------


def test_aggregate_revenue_by_region_and_month():
    df = load_sales(FIXTURE)
    clean_df, _ = clean(df)
    agg = aggregate(clean_df)
    assert agg.by_region.to_dict() == {"North": 310.0, "South": 620.0}
    assert agg.by_month.to_dict() == {"2024-01": 470.0, "2024-02": 460.0}


def test_report_contains_formatted_totals():
    df = load_sales(FIXTURE)
    clean_df, _ = clean(df)
    text = report(aggregate(clean_df))
    assert "North" in text
    assert "310.00" in text
    assert "South" in text
    assert "620.00" in text
    assert "2024-01" in text
    assert "470.00" in text
    assert "2024-02" in text
    assert "460.00" in text


# --- run (argparse front-end) --------------------------------------------


def test_run_writes_report_to_output_path(tmp_path):
    output = tmp_path / "report.txt"
    exit_code = run([str(FIXTURE), str(output)])
    assert exit_code == 0
    text = output.read_text()
    assert "310.00" in text
    assert "620.00" in text


def test_run_missing_input_returns_nonzero_and_writes_nothing(tmp_path, capsys):
    output = tmp_path / "report.txt"
    exit_code = run([str(tmp_path / "missing.csv"), str(output)])
    assert exit_code != 0
    assert not output.exists()
    captured = capsys.readouterr()
    assert captured.err != ""
