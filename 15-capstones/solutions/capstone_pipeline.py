# Capstone B: a pandas data pipeline over a messy sales CSV. Concepts:
# loading/validating files, cleaning with pandas, custom exceptions,
# EAFP-style coercion, and an argparse front-end.
# Run: uv run pytest 15-capstones -k capstone_pipeline

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

DATE_FORMATS = ("%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y")
_BLANKLIKE = {"", "N/A", "NA", "NAN", "NONE", "NULL"}


class PipelineError(Exception):
    """Raised when the sales file can't be loaded."""


@dataclass
class SalesAggregate:
    """Revenue rollups produced by `aggregate`.

    by_region: total revenue per region, indexed by region name.
    by_month: total revenue per calendar month, indexed by "YYYY-MM".
    """

    by_region: pd.Series
    by_month: pd.Series


def load_sales(path: str | Path) -> pd.DataFrame:
    """Load the raw sales CSV as-is (every column read as text; cleaning
    happens in `clean`, not here).

    Raises PipelineError if `path` doesn't exist.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise PipelineError(f"sales file not found: {file_path}")
    return pd.read_csv(file_path, dtype=str, keep_default_na=False)


def _blank(value: str) -> bool:
    return value.strip().upper() in _BLANKLIKE


def _parse_date(raw: str) -> pd.Timestamp | None:
    text = raw.strip()
    for fmt in DATE_FORMATS:
        try:
            return pd.to_datetime(text, format=fmt)
        except ValueError:
            continue
    return None


def _parse_money(raw: str) -> float | None:
    text = raw.strip().replace("$", "").replace(",", "")
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def clean(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """Clean a raw sales dataframe (as returned by `load_sales`).

    Steps, in order: normalize region text (strip + title case); drop
    exact duplicate rows (keep the first occurrence); then, per
    remaining row, parse the date against several known formats, coerce
    quantity to a positive int and price to a float (stripping "$" and
    ","), and drop any row missing a required field, failing to parse,
    or with a non-positive quantity.

    Every dropped row is recorded in the returned issues list as
    "<order_id>: <reason>", in the order the row was encountered
    (duplicates first, then other bad rows in file order).

    Returns (clean_df, issues). clean_df has columns order_id, date
    (datetime64), region (str), product (str), quantity (int), price
    (float).
    """
    working = df.copy()
    working["region"] = working["region"].astype(str).str.strip().str.title()

    is_dup = working.duplicated(keep="first")
    issues: list[str] = [
        f"{row.order_id}: duplicate row" for row in working.loc[is_dup].itertuples()
    ]
    working = working.loc[~is_dup].reset_index(drop=True)

    kept_rows: list[dict[str, object]] = []
    for row in working.itertuples(index=False):
        order_id = row.order_id
        region = row.region
        product = str(row.product).strip()
        quantity_raw = str(row.quantity)
        price_raw = str(row.price)

        if _blank(region):
            issues.append(f"{order_id}: missing region")
            continue
        if _blank(product):
            issues.append(f"{order_id}: missing product")
            continue
        if _blank(quantity_raw):
            issues.append(f"{order_id}: missing quantity")
            continue
        if _blank(price_raw):
            issues.append(f"{order_id}: missing price")
            continue

        parsed_date = _parse_date(str(row.date))
        if parsed_date is None:
            issues.append(f"{order_id}: invalid date")
            continue

        try:
            quantity = int(quantity_raw.strip())
        except ValueError:
            issues.append(f"{order_id}: invalid quantity")
            continue
        if quantity <= 0:
            issues.append(f"{order_id}: invalid quantity")
            continue

        price = _parse_money(price_raw)
        if price is None or price < 0:
            issues.append(f"{order_id}: invalid price")
            continue

        kept_rows.append(
            {
                "order_id": order_id,
                "date": parsed_date,
                "region": region,
                "product": product,
                "quantity": quantity,
                "price": price,
            }
        )

    clean_df = pd.DataFrame(
        kept_rows, columns=["order_id", "date", "region", "product", "quantity", "price"]
    )
    if not clean_df.empty:
        clean_df["date"] = pd.to_datetime(clean_df["date"])
        clean_df["quantity"] = clean_df["quantity"].astype(int)
        clean_df["price"] = clean_df["price"].astype(float)
    return clean_df, issues


def aggregate(df: pd.DataFrame) -> SalesAggregate:
    """Compute total revenue (quantity * price) by region and by month.

    `df` must be shaped like `clean`'s output (typed date/quantity/price
    columns). Both Series in the result are sorted by index.
    """
    revenue = df["quantity"] * df["price"]
    by_region = revenue.groupby(df["region"]).sum().sort_index()
    by_region.name = "revenue"
    month = df["date"].dt.strftime("%Y-%m")
    by_month = revenue.groupby(month).sum().sort_index()
    by_month.name = "revenue"
    return SalesAggregate(by_region=by_region, by_month=by_month)


def report(agg: SalesAggregate) -> str:
    """Render a SalesAggregate as a plain-text report.

    Two sections, "Revenue by region" and "Revenue by month", each
    formatted as "  <label>: $<amount, 2dp>" lines.
    """
    lines = ["Sales Report", "=" * len("Sales Report"), "", "Revenue by region:"]
    for region, total in agg.by_region.items():
        lines.append(f"  {region:<10}: ${total:,.2f}")
    lines.append("")
    lines.append("Revenue by month:")
    for month, total in agg.by_month.items():
        lines.append(f"  {month:<10}: ${total:,.2f}")
    return "\n".join(lines) + "\n"


def run(argv: list[str]) -> int:
    """Argparse front-end: `run([input_csv, output_txt])`.

    Loads, cleans, aggregates, and writes the text report to the output
    path. Prints how many rows were dropped (if any) to stderr.
    Returns 0 on success, 1 if the input file couldn't be loaded.
    """
    parser = argparse.ArgumentParser(
        prog="capstone_pipeline",
        description="Clean a messy sales CSV and write a revenue report.",
    )
    parser.add_argument("input", help="path to the messy sales CSV")
    parser.add_argument("output", help="path to write the text report to")
    args = parser.parse_args(argv)

    try:
        raw = load_sales(args.input)
    except PipelineError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    clean_df, issues = clean(raw)
    agg = aggregate(clean_df)
    Path(args.output).write_text(report(agg))
    if issues:
        print(f"dropped {len(issues)} bad row(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))
