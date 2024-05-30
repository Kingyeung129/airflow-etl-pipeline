import json
import os

import pandas as pd


def check_scraped_data_exists():
    fname = os.environ.get("SCRAPED_DATA_FILE")
    if os.path.isfile(fname):
        print("Scraped file exists. Proceeding with data transformation...")
        return True
    return False


def read_scraped_data(file=os.environ.get("SCRAPED_DATA_FILE")):
    print("Reading scraped data file...")
    data = json.loads(open(file).read)
    return data


def transform_data(data):
    print("Transforming data...")
    return


def main():

    data = read_scraped_data()
    transform_data(data)
    print("Loading script execution completed!")
    return


if __name__ == "__main__":
    main()
