import os
import pathlib
import unittest
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional

import requests
from dotenv import load_dotenv
from pytion import auth, helper
from pytion.core import NotionClient
from pytion.schemas import NewThingSchema
from pytion.settings import settings

load_dotenv()

TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
ROOT = pathlib.Path(__file__).parents[1]


def _teardown_data(block_id):
    response = requests.delete(
        url=f"https://api.notion.com/v1/blocks/{block_id}",
        headers=auth.AuthorizationHeader(authorization=TOKEN).dict(),
    )
    if "status" not in response.json():
        return True
    return False


class TestSettings(unittest.TestCase):
    def test_token(self):
        self.assertEqual(settings.NOTION_TOKEN, TOKEN)

    def test_database_id(self):
        self.assertEqual(settings.NOTION_DATABASE_ID, DATABASE_ID)


class TestAuth(unittest.TestCase):
    def test_AuthorizationHeader(self):
        header = auth.AuthorizationHeader(
            authorization="token",
            notion_version="2022-01-01",
        )

        expected = {
            "Authorization": "Bearer token",
            "Notion-Version": "2022-01-01",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        self.assertDictEqual(header.dict(), expected)


class TestHelper(unittest.TestCase):
    HTML: Optional[str] = None
    parser: Optional[helper.HTMLBodyParser] = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.HTML = ROOT.joinpath("resources/testdata.html").read_text("utf-8")
        cls.parser = helper.HTMLBodyParser(cls.HTML)

    def test__parse_issue(self):
        self.assertNotEqual(self.parser._parse_issue(), {})

    def test__parse_entity(self):
        self.assertNotEqual(self.parser._parse_entity(), [])

    def test_get(self):
        self.assertNotEqual(self.parser.get(), [])


class TestCore(unittest.TestCase):
    client: Optional[NotionClient] = None
    items: Optional[List[NewThingSchema]] = None
    blocks: Optional[List[str]] = []
    _thread_pool = ThreadPoolExecutor(max_workers=2)

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = NotionClient(settings.NOTION_TOKEN, settings.NOTION_DATABASE_ID)

        HTML = ROOT.joinpath("resources/testdata.html").read_text("utf-8")
        cls.items = helper.HTMLBodyParser(HTML).get()

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.blocks:
            with cls._thread_pool as worker:
                _ = worker.map(_teardown_data, cls.blocks)

    def test_query_database(self):
        response = self.client.query_database()
        self.assertEqual(response.get("status"), None)

    def test_properties(self):
        properties = set(self.client.properties)
        expected = {"id", "name", "price", "source", "url", "issue", "author"}

        self.assertSetEqual(properties, expected)

    def test_add_row(self):
        record = self.items[0]
        data = self.client.add_row(record)

        self.assertEqual(data.get("status"), None)
        self.blocks.append(data["id"])

    def test_add_rows(self):
        data = self.client.add_rows(self.items)
        for response in data:
            with self.subTest(response=response):
                self.assertEqual(response.get("status"), None)
                self.blocks.append(response["id"])
