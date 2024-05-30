import pytz

from datetime import datetime
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from crypto_etl import scrape, transform, load


time_zone = pytz.timezone("Asia/Singapore")
default_args = {
    "owner": "admin",
    "start_date": datetime(2024, 5, 31, 0, 48, 0, tzinfo=time_zone),
    "retries": 1,
    "catchup": False,
}

with DAG(
    dag_id="crypto_etl", default_args=default_args, schedule_interval="*/5 * * * *"
) as dag:

    task_start = DummyOperator(task_id="task_start")

    python_scrape = PythonOperator(task_id="python_scrape", python_callable=scrape.main)

    python_transform = PythonOperator(
        task_id="python_transform", python_callable=transform.main
    )

    python_load = PythonOperator(task_id="python_load", python_callable=load.main)

    task_end = DummyOperator(task_id="task_end")

task_start >> python_scrape >> python_transform >> python_load >> task_end
