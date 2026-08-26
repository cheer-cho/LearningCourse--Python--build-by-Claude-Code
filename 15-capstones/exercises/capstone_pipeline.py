# Capstone B: build a pandas data pipeline over a messy sales CSV.
# Concepts: loading/validating files, cleaning with pandas, custom
# exceptions, EAFP-style coercion, an argparse front-end. Brief: LESSON.md.
# Run: uv run pytest 15-capstones -k capstone_pipeline

from __future__ import annotations

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
    raise NotImplementedError


def clean(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """Clean a raw sales dataframe (as returned by `load_sales`).

    Steps, in order: normalize region text (strip + title case); drop
    exact duplicate rows (keep the first occurrence); then, per
    remaining row, parse the date against DATE_FORMATS (in order),
    coerce quantity to a positive int and price to a float (stripping
    "$" and ","), and drop any row missing a required field, failing to
    parse, or with a non-positive quantity.

    Every dropped row is recorded in the returned issues list as
    "<order_id>: <reason>", in the order the row was encountered
    (duplicates first, then other bad rows in file order). Reasons:
    "duplicate row", "missing region", "missing product",
    "missing quantity", "missing price", "invalid quantity",
    "invalid price", "invalid date".

    Returns (clean_df, issues). clean_df has columns order_id, date
    (datetime64), region (str), product (str), quantity (int), price
    (float).
    """
    raise NotImplementedError


def aggregate(df: pd.DataFrame) -> SalesAggregate:
    """Compute total revenue (quantity * price) by region and by month.

    `df` must be shaped like `clean`'s output (typed date/quantity/price
    columns). Both Series in the result are sorted by index.
    """
    raise NotImplementedError


def report(agg: SalesAggregate) -> str:
    """Render a SalesAggregate as a plain-text report.

    Two sections, "Revenue by region" and "Revenue by month", each
    formatted as "  <label>: $<amount, 2dp>" lines.
    """
    raise NotImplementedError


def run(argv: list[str]) -> int:
    """Argparse front-end: `run([input_csv, output_txt])`.

    Loads, cleans, aggregates, and writes the text report to the output
    path. Prints how many rows were dropped (if any) to stderr.
    Returns 0 on success, 1 if the input file couldn't be loaded.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))
