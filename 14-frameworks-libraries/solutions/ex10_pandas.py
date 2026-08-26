import pandas as pd


def to_frame(records: list[dict[str, object]]) -> pd.DataFrame:
    return pd.DataFrame.from_records(records)


def revenue_by_region(df: pd.DataFrame) -> dict[str, float]:
    return df.groupby("region")["revenue"].sum().to_dict()


def add_margin_column(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(margin=df["revenue"] - df["cost"])


def top_products(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.sort_values("revenue", ascending=False, kind="stable").head(n).reset_index(drop=True)
