from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipeline import run


def execute_etl():
    run("data/raw/orders.csv", "data/processed/orders_clean.csv")

with DAG(
    "enterprise_order_etl",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "data-engineering"],
) as dag:
    etl = PythonOperator(task_id="transform_orders", python_callable=execute_etl)
