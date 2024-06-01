# Dockerfile
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3.11-dev \
    gcc curl wget gnupg2 postgresql-common
    # && rm -rf /var/lib/apt/lists/*

# Install postgres client version 16
RUN yes '' | /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
RUN apt-get install -y postgresql-client-16 libpq-dev

# Set up Python 3.11 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Install Airflow using pip
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && python3 -m venv /opt/airflow \
    && /opt/airflow/bin/pip install --upgrade pip \
    && /opt/airflow/bin/pip install apache-airflow

# Copy dag files
RUN mkdir -p /airflow-etl-pipeline/dags
COPY ./dags /airflow-etl-pipeline/dags

WORKDIR /airflow-etl-pipeline

# Set environment variables
COPY .env .
ENV AIRFLOW_HOME=/airflow-etl-pipeline

# Install Python dependencies
COPY requirements.txt .
RUN /opt/airflow/bin/pip install -r requirements.txt

# Set up Airflow configuration
COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Copy initialization scripts
COPY setup/airflow/init_airflow.sh /init_airflow.sh
RUN chmod +x /init_airflow.sh

ENTRYPOINT ["/init_airflow.sh"]
