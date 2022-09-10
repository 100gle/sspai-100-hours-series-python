import random
from string import ascii_letters, digits, punctuation
from typing import List, Optional, Union
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from pytion._types import Numeric


# ===============
# Base type
# ===============
class IdProvider:

    letters = "".join([ascii_letters, punctuation, digits])

    def __init__(self, version="string") -> None:
        self.version = version

    def __call__(self, *args, **kwargs) -> str:
        if self.version == "string":
            return "".join(random.choices(self.letters, k=5))
        return str(uuid4())


class Property(BaseModel):
    id: Union[str, UUID] = Field(default_factory=IdProvider())
    type: Optional[str]


# ===============
# String type
# ===============
class Content(BaseModel):
    content: str


class TextProperty(BaseModel):
    type: str = "text"
    text: Content


class RichTextProperty(Property):
    type: str = "rich_text"
    rich_text: List[TextProperty]


class TitleProperty(Property):
    type: str = "title"
    title: List[TextProperty]


class StringProperty(dict):
    def __new__(cls, value: str, type=None, *args, **kwargs):
        data = [TextProperty(text=Content(content=value))]
        if type == "title":
            return TitleProperty(title=data)
        return RichTextProperty(rich_text=data)


# ===============
# Numeric type
# ===============
class NumberProperty(Property):
    type: str = "number"
    number: Numeric


# ===============
# URL type
# ===============
class URLProperty(Property):
    type: str = "url"
    url: Optional[str]
