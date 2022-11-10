import requests


def save_file(data, file_name: str) -> None:
    """Saves data into file in current directory"""
    with open(file_name, 'w+') as f:
        f.write(data)


def download_file(url: str, file_name: str) -> None:
    """Saves content from URL as a text to file."""
    r = requests.get(url)
    r.raise_for_status()
    save_file(r.text, file_name)
