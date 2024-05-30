import json

import psycopg2
from dotenv import load_dotenv

load_dotenv()


# Test database connection
def test_db_connection():
    return False


def read_transformed_data_from_file(file="transformed_data.json"):
    data = json.loads(open(file).read())
    return data


def load_data(data=[]):
    json.dumps(data)
    return


def main():
    test_db_connection()
    data = read_transformed_data_from_file()
    load_data(data)
    print("Loading script execution completed!")
    return


if __name__ == "__main__":
    main()
