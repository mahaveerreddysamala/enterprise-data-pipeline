import pandas as pd
from src.pipeline import transform


def test_transform_deduplicates_and_creates_month():
    df = pd.DataFrame([
        {"customer_id": 1, "order_id": "A1", "order_date": "2026-01-15", "amount": 100, "status": "paid"},
        {"customer_id": 1, "order_id": "A1", "order_date": "2026-01-15", "amount": 120, "status": "paid"},
    ])
    result = transform(df)
    assert len(result) == 1
    assert result.iloc[0]["net_amount"] == 120
    assert result.iloc[0]["order_month"] == "2026-01"
