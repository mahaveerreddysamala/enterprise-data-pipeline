from pathlib import Path
import pandas as pd

REQUIRED = {"customer_id", "order_id", "order_date", "amount", "status"}


def validate(df: pd.DataFrame) -> None:
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if df["customer_id"].isna().any() or df["order_id"].isna().any():
        raise ValueError("Customer and order identifiers cannot be null")


def transform(df: pd.DataFrame) -> pd.DataFrame:
    validate(df)
    out = df.copy()
    out["order_date"] = pd.to_datetime(out["order_date"], errors="coerce")
    out["amount"] = pd.to_numeric(out["amount"], errors="coerce").fillna(0)
    out = out.dropna(subset=["order_date"])
    out = out.drop_duplicates(subset=["order_id"], keep="last")
    out["order_month"] = out["order_date"].dt.to_period("M").astype(str)
    out["net_amount"] = out["amount"].clip(lower=0)
    return out


def run(input_file: str, output_file: str) -> None:
    df = pd.read_csv(input_file)
    result = transform(df)
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_file, index=False)


if __name__ == "__main__":
    run("data/raw/orders.csv", "data/processed/orders_clean.csv")
