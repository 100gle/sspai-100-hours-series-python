import logging
from concurrent.futures import ThreadPoolExecutor

import requests
from pytion.core import NotionClient
from pytion.helper import HTMLBodyParser
from pytion.settings import settings

logging.basicConfig(
    level=settings.PYTION_DEBUG,
    format=settings.PYTION_LOG_FORMAT,
    style="{",
)
client = NotionClient(
    token=settings.NOTION_TOKEN,
    database_id=settings.NOTION_DATABASE_ID,
)


def query(url):
    response = requests.get(url=url)
    items = HTMLBodyParser(response.text, url=url)
    records = items.get()
    client.add_rows(records)
    return True


def main():
    urls = [
        "https://sspai.com/post/74158",
        "https://sspai.com/post/73964",
        "https://sspai.com/post/73826",
        "https://sspai.com/post/73036",
        "https://sspai.com/post/68115",
    ]

    with ThreadPoolExecutor(2) as w:
        w.map(query, urls)


if __name__ == "__main__":
    main()
