from pydantic import BaseModel
from pytion._types import DictLike

__all__ = ("NotionAPI", "ParentSchema", "PageSchema")

BASE_URL = "https://api.notion.com/v1"


class NotionAPI:
    # databases
    QUERY_DATABASE_BY_ID: str = BASE_URL + "/databases/{database_id}/query"

    # pages
    QUERY_PAGE_BY_ID: str = BASE_URL + "/pages/{page_id}"
    CREATE_PAGE: str = BASE_URL + "/pages"


class ParentSchema(BaseModel):
    type: str = "database_id"
    database_id: str


class PageSchema(BaseModel):
    parent: ParentSchema
    properties: DictLike
