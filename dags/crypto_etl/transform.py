import json
import os
from datetime import datetime
import pytz

import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def check_scraped_data_exists(fp):
    if os.path.isfile(fp):
        print("Scraped file exists. Proceeding with data transformation...")
        return True
    return False


def read_scraped_data(fp):
    print("Reading scraped data file...")
    data = json.loads(open(fp).read())
    return data


def transform_data(data):
    print("Transforming data...")
    try:
        df = pd.json_normalize(data["prices"])
        # Convert all column headers to lower case
        df.columns = df.columns.str.lower()
        # Convert all column to string datatype
        df = df.astype(str)
        df["timestamp"] = pd.json_normalize(data)["timestamp"]
        # Change timestamp from GMT to Singapore Timezone and convert to sql compliant
        gmt_timestamp = pytz.timezone("GMT").localize(
            datetime.strptime(df["timestamp"].iloc[0], "%a, %d %b %Y %H:%M:%S %Z")
        )
        df.loc[0, "timestamp"] = gmt_timestamp.astimezone(
            pytz.timezone("Asia/Singapore")
        ).strftime("%Y-%m-%d %H:%M:%S")
        fp = os.path.join(
            os.path.dirname(__file__),
            os.environ.get("DATA_DIR"),
            os.environ.get("TRANSFORMED_DATA_FILE"),
        )
    except Exception as e:
        print(e)
        print("Failed transforming data.")
        return None
    print(df)
    print("Successfully transformed data.")
    return df


def save_data(data=pd.DataFrame()):
    print("Saving transformed data...")
    fp = os.path.join(
        os.path.dirname(__file__),
        os.environ.get("DATA_DIR"),
        os.environ.get("TRANSFORMED_DATA_FILE"),
    )
    print(f"Output file path will be: {fp}")
    data.to_csv(fp, index=False)
    return True


def main():
    fp = os.path.join(
        os.path.dirname(__file__),
        os.environ.get("DATA_DIR"),
        os.environ.get("SCRAPED_DATA_FILE"),
    )
    if not check_scraped_data_exists(fp):
        return False
    data = read_scraped_data(fp)
    data = transform_data(data)
    save_data(data)
    print("Loading script execution completed!")
    return True


if __name__ == "__main__":
    main()
