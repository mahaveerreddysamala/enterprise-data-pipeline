from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def validate_sources():
    print('Validate source schema, freshness and null thresholds')


def build_dimensions():
    print('Build customer and product dimensions with incremental keys')


def load_facts():
    print('Load incremental order facts and update warehouse aggregates')

with DAG('warehouse_refresh', start_date=datetime(2026, 1, 1), schedule='0 2 * * *', catchup=False) as dag:
    validation = PythonOperator(task_id='validate_sources', python_callable=validate_sources)
    dimensions = PythonOperator(task_id='build_dimensions', python_callable=build_dimensions)
    facts = PythonOperator(task_id='load_facts', python_callable=load_facts)
    validation >> dimensions >> facts
