import logging
import re
from functools import partial
from pprint import pformat
from typing import List, Optional

import bs4
from pytion._types import DictLike
from pytion.schemas import NewThingSchema, ProductInfoSchema

LOG = logging.getLogger("pytion.helper")
pformat = partial(pformat, depth=2)


class HTMLBodyParser:
    _REGEX_ISSUE = re.compile(r"(?P<issue>\d+).*")
    _REGEX_TITLE = re.compile(r"@(?P<author>.+)(?:[:：])(?P<name>.+)")  # noqa:ignore
    _REGEX_PRICE_TAG = re.compile(r"价格.*")
    _REGEX_SOURCE_TAG = re.compile(r"渠道|平台")

    def __init__(self, html: str, url: Optional[str] = None) -> None:
        self.html = bs4.BeautifulSoup(html, "html.parser")
        self.raw_html = self.html.prettify()
        self.url = url

    def _parse_issue(self) -> DictLike:
        title = self.html.select("title")[0]
        return self._REGEX_ISSUE.search(title.text).groupdict()

    def _parse_entity(self) -> List[DictLike]:
        data = []

        starts = self.html.find_all("h2")
        for h2 in starts:
            info = ProductInfoSchema()

            title = self._REGEX_TITLE.search(h2.text).groupdict()
            ul = h2.find_next("ul")
            sources = ul.find_next(text=self._REGEX_SOURCE_TAG)
            prices = ul.find_next(text=self._REGEX_PRICE_TAG)

            if sources:
                info.source = sources

            if prices:
                info.price = prices
            data.append(dict(**title, **info.dict()))
        return data

    def get(self) -> List[NewThingSchema]:
        data = []
        issue = self._parse_issue()
        entities = self._parse_entity()

        for index, entity in enumerate(entities, start=1):
            newthing = NewThingSchema(id=index, **entity, **issue)
            if self.url:
                newthing.url = self.url
            data.append(newthing)

        LOG.debug(f"all data: {pformat(data)}")
        return data
