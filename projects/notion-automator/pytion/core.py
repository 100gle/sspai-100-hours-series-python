import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from textwrap import shorten
from typing import List

import requests
from pytion._types import DictLike
from pytion.auth import AuthorizationHeader
from pytion.exception import APIQueryException
from pytion.helper import pformat
from pytion.schemas import (
    NewThingSchema,
    NotionAPI,
    NumberProperty,
    PageSchema,
    ParentSchema,
    StringProperty,
    URLProperty,
)

__all__ = "NotionClient"

LOG = logging.getLogger("pytion.core")


class Record:
    def __init__(
        self,
        id: int,
        author: str,
        name: str,
        price: str,
        source: str,
        url: str,
        issue: int,
    ):
        self.id = NumberProperty(number=id)
        self.author = StringProperty(value=author)
        self.name = StringProperty(value=name, type="title")
        self.price = StringProperty(value=price)
        self.source = StringProperty(value=source)
        self.url = URLProperty(url=url)
        self.issue = NumberProperty(number=issue)

    def dict(self):
        target = {}
        for key in self.__dict__.keys():
            if not key.startswith("_"):
                target[key] = self.__dict__[key]
        return target


class NotionClient:
    def __init__(self, token: str, database_id: str) -> None:
        self._token = token
        self._database_id = database_id
        self._auth = AuthorizationHeader(authorization=token).dict()
        self._database_info: DictLike = {}
        self._properties: DictLike = {}
        self._parent = ParentSchema(database_id=self._database_id)

    def __repr__(self) -> str:
        masked_token = self._mask_token(self._token)
        return f"NotionClient<token={masked_token}, database={self._database_id}>"

    __str__ = __repr__

    def _mask_token(self, token: str) -> str:
        return shorten(token, width=10, placeholder="...")

    def query_database(self) -> "DictLike":
        payload = {"page_size": 100}
        url = NotionAPI.QUERY_DATABASE_BY_ID.format(database_id=self._database_id)
        response = requests.post(url, headers=self._auth, json=payload)
        data = response.json()
        if response.status_code != 200:
            LOG.debug("query failed, see exception as below:")
            raise APIQueryException(status_code=response.status_code, detail=data)

        # Caching the database info
        self._database_info = data
        LOG.debug(f"database response is: {pformat(data)}")
        return data

    @property
    def properties(self):
        return self._extract_properties()

    def _extract_properties(self) -> List[str]:
        if not self._database_info:
            self.query_database()
        properties = self._database_info["results"][0]["properties"]
        LOG.debug(f"properties are: {pformat(properties)}")

        return list(properties.keys())

    def add_row(self, record: NewThingSchema) -> DictLike:
        properties = Record(**record.dict()).dict()
        params = PageSchema(parent=self._parent, properties=properties)
        response = requests.post(
            NotionAPI.CREATE_PAGE, json=params.dict(), headers=self._auth
        )
        data = response.json()
        if response.status_code != 200:
            LOG.debug("add data failed, see exception as below:")
            raise APIQueryException(status_code=response.status_code, detail=data)

        LOG.debug(f"page response is: {pformat(data)}")
        return data

    def add_rows(self, records: List[NewThingSchema]) -> List[DictLike]:
        responses = []
        with ThreadPoolExecutor(max_workers=2) as worker:
            features = [
                worker.submit(self.add_row, record=record) for record in records
            ]

            for feature in as_completed(features):
                responses.append(feature.result())

        return responses
