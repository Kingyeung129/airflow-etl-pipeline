import json
import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import urllib.parse

load_dotenv()

db_host = os.getenv("DB_PG_HOST_NAME")
db_port = os.getenv("DB_PG_PORT")
db_name = os.getenv("DB_PG_DB_NAME")
db_user = os.getenv("DB_PG_USER")
db_pass = urllib.parse.quote_plus(os.getenv("DB_PG_PASS"))
db_schema = os.getenv("DB_PG_SCHEMA")
db_conn_str = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"


# Create database conenction str and engine
def init_db_engine():
    print(
        f"Connection configuration as follow: {db_user}@{db_host} on PORT {db_port} to DATABASE {db_name} SCHEMA {db_schema}"
    )
    # Create the connection to the PostgreSQL database
    engine = create_engine(db_conn_str)
    return engine


# Test database connection
def test_db_connection(engine=create_engine(db_conn_str)):
    try:
        # Attempt to connect to the database
        with engine.connect() as connection:
            print("Connection to the PostgreSQL database was successful!")
            return True
    except SQLAlchemyError as e:
        # Print any error messages if the connection fails
        print(f"Error: {e}")
    return False


def read_transformed_data_from_file(file=os.getenv("TRANSFORMED_DATA_FILE")):
    print("Reading transformed data file...")
    fp = os.path.join(
        os.path.dirname(__file__),
        os.getenv("DATA_DIR"),
        os.getenv("TRANSFORMED_DATA_FILE"),
    )
    df = pd.read_csv(fp)
    return df


def load_data(data=pd.DataFrame(), engine=create_engine(db_conn_str)):
    print("Loading data to database...")
    table_name = "crypto_price"
    try:
        # Load data into the PostgreSQL table, specifying the schema
        res = data.to_sql(
            table_name, engine, schema=db_schema, if_exists="append", index=False
        )
        print(
            f"Data loaded successfully into the table '{table_name}' in schema '{db_schema}'. Records inserted {res}."
        )
    except Exception as e:
        # Print any error messages if data loading fails
        print(f"Error loading data: {e}")
    loaded_data = pd.read_sql(f"SELECT * FROM {db_schema}.crypto_price", con=engine)
    print(loaded_data.iloc[-1])
    return


def main():
    engine = init_db_engine()
    if not test_db_connection(engine):
        return False
    data = read_transformed_data_from_file()
    load_data(data, engine=engine)
    print("Loading script execution completed!")
    return True


if __name__ == "__main__":
    main()
