# Documentation

## Purpose

This repo is a personal project to build and learn how to develop an apache airflow data pipeline that performs a full ETL process. From scraping of data, transforming and loading the data to a database.

## Introduction

Web scraping will be done by calling API from a crypto currency API provider. Data will then be stored as flat files in a data directory specified by environment variables. Transformation will be performed to transform data to database schema. After transformation, loading will be performed to load data into a relational database. Finally, a visualization tool will connect to the relational database to query and visualize the ETL data.

## Pre-requisites

1. Linux distro (tested on Ubuntu 22.04)
2. Install python version 3.11.9 and virtual environment (tested on this version)
3. Postgres database with schema and priviledges setup (this will be used for airflow database initialization and etl project datbase as well)
4. Internet connection for web requests to scraped data
5. Metabase server to visualize ETL data from database


## Instructions

<i>Note that the below instructions is for Linux debian distributions (tested on Ubuntu 22.04)</i>

1. Install postgres client and postgres library for psycopg2 package to work

<pre><code>sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
sudo apt install postgres-client-16 libpq-dev</code></pre>

2. Create and activate python virtual environment. Please ensure python version is at least >=3.11 and above. Please refer to the following link on installing python from deadsnakes ppa. Remember to install the venv package as well.

<i>(Optional) Command will be the following</i>
<pre><code>sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv</code></pre>

3. Clone this repo, change directory and create python virtual environment
<pre><code># Change directory into git repo
cd airflow-etl-pipeline

# Note that command here for creating virtual environment may vary depending on how python is installed
python3.11 -m venv ".venv"

# Activate python virtual env
source ./.venv/bin/activate</code></pre>

4. Install python packages

<pre><code>pip install -r requirements.txt</code></pre>

5. Change environment variables and confuration in airflow config and .env file. Rename "[.env.bak](.env.bak)" as ".env" and "[airflow.cfg.bak](airflow.cfg.bak)" as "airflow.cfg".

6. Set airflow home environment variable (**IMPORTANT**) to ensure airflow can find and read the dags folder in repo
<pre><code># Change according to the path of the cloned repo
echo "export AIRFLOW_HOME=~/airflow-etl-pipeline" >> ~/.bashrc

# Reloading terminal and .bashrc config
source ~/.bashrc

# Ensure that AIRFLOW_HOME variable is set
echo $AIRFLOW_HOME
</code></pre>

7. Initialize airflow database and create user

<pre><code># Initialize airflow database
airflow db init

# Create airflow admin account by changing flags below accordingly
airflow users create \
          --username admin \
          --firstname FIRST_NAME \
          --lastname LAST_NAME \
          --role Admin \
          --email admin@example.org \
          --password PASSWORD
</code></pre>

8. Start airflow scheduler and webserver

<pre><code># You will need to split terminal to run both processes
airflow scheduler
airflow webserver
</code></pre>

Visit http://localhost:8080 on a web browser to view airflow webui and run dags from there.