import json
import os

import requests as req
from dotenv import load_dotenv

load_dotenv()


def fetch_api():
    print("Fetching API...")
    api, api_key = (os.environ.get("API_URL"), os.environ.get("API_KEY"))
    res = req.get(api)
    if res.status_code == 200:
        print("API successfully called...")
        print(res.json())
        return res.json()
    print("API call failed...")
    return False


def save_data(data=[]):
    print("Saving data from API...")
    fp = os.path.join(
        os.path.dirname(__file__),
        os.environ.get("DATA_DIR"),
        os.environ.get("SCRAPED_DATA_FILE"),
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
        print(f"Data saved to {os.environ.get('SCRAPED_DATA_FILE')}.")
    else:
        print("Could not save json data to flat file.")
    print("Scraping script execution completed!")
    return True


if __name__ == "__main__":
    main()
