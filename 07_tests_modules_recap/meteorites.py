import os
import json
from datetime import datetime, timedelta
from random import randrange
from my_utils import download_file


DATA_FILE = 'meteorites.json'
URL_NASA_METEORIT_LANDINGS_API = "https://data.nasa.gov/resource/gh4g-9sfh.json"


def load_meteorites(file_name: str = DATA_FILE) -> None:
    with open(file_name) as f:
        return json.loads(f.read())


def get_last_meteorit(data: str) -> dict:
    if not data:
        print("Nothing fell down last day :(")

    return load_meteorites(data)[0]


def get_random_meteorit(data: str) -> dict:
    meteorites = load_meteorites(data)

    return meteorites[randrange(len(meteorites))]


def print_summary(meteorit_info: str, secret_info: bool = False) -> None:
    for k, v in meteorit_info.items():
        if not k.startswith(':') or secret_info:
            print(f'{k}: {v}')
            print('{}: {}'.format(k, v))


# This could be refactored to do check in separate function.
def get_latest_data(url: str, file_name: str, max_age_hours: int = 24) -> None:
    yesterday = datetime.now() - timedelta(hours=max_age_hours)
    file_modified_at = datetime.fromtimestamp(os.path.getmtime(file_name))

    if file_modified_at < yesterday:
        print('Downloading latest data...')
        download_file(url, file_name)

    # print('Cool, already have latest data...')


if __name__ == '__main__':
    print("Meteorite of the day is:\n")
    get_latest_data(URL_NASA_METEORIT_LANDINGS_API, DATA_FILE)
    # print_summary(get_last_meteorit(DATA_FILE))
    print_summary(get_random_meteorit(DATA_FILE))
