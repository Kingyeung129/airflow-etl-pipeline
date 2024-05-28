import json
import os

import requests as req
from dotenv import load_dotenv

load_dotenv()


def fetch_api():
    print("Fetching API...")
    api, api_key = (os.environ.get("API_URL"), os.environ.get("API_KEY"))
    res = req.get(api, headers={"api-key": api_key})
    if res.status_code == 200:
        print("API successfully called...")
        return res.json()
    print("API call failed...")
    return False


def save_data(data=[]):
    print("Saving data from API...")
    json.dumps(data)
    return


def main():
    data = fetch_api()
    if not data:
        return
    save_data(data)
    print("Scraping script execution completed!")
    return


if __name__ == "__main__":
    main()
