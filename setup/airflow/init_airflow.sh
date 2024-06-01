#!/bin/bash

# Initialize the Airflow DB
/opt/airflow/bin/airflow db init

# Create an admin user
/opt/airflow/bin/airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password P@ssw0rd

# Start airflow scheduler and webserver
/opt/airflow/bin/airflow scheduler &
/opt/airflow/bin/airflow webserver