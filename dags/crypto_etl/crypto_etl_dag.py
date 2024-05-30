from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

# from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from crypto_etl import scrape

default_args = {"owner": "admin", "start_date": datetime(2024, 5, 29, 12, 0, 0)}

with DAG(
    dag_id="crypto_etl", default_args=default_args, schedule_interval="@once"
) as dag:

    task_start = DummyOperator(task_id="task_start")

    python_scrape = PythonOperator(task_id="test_python", python_callable=scrape.main)

    task_end = DummyOperator(task_id="task_end")

task_start >> python_scrape >> task_end
