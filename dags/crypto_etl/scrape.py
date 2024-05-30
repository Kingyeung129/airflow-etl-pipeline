import json
import os

import requests as req
from dotenv import load_dotenv

load_dotenv()


def fetch_api():
    print("Fetching API...")
    api, api_key = (os.getenv("API_URL"), os.getenv("API_KEY"))
    res = req.get(api)
    if res.status_code == 200:
        print("API successfully called...")
        print(res.json())
        timestamp = res.headers.get("Date")
        prices = res.json()
        data = {"timestamp": timestamp, "prices": prices}
        return data
    print("API call failed...")
    return False


def save_data(data=[]):
    print("Saving data from API...")
    fp = os.path.join(
        os.path.dirname(__file__),
        os.getenv("DATA_DIR"),
        os.getenv("SCRAPED_DATA_FILE"),
    )
    print(f"Output file path will be: {fp}")
    with open(fp, "w") as f:
        json.dump(data, f)
    return True


def main():
    data = fetch_api()
    if not data:
        return False
    save_file_status = save_data(data)
    if save_file_status:
        print(f"Data saved to {os.getenv('SCRAPED_DATA_FILE')}.")
    else:
        print("Could not save json data to flat file.")
    print("Scraping script execution completed!")
    return True


if __name__ == "__main__":
    main()
