from typing import Optional

from pydantic import BaseModel, Field

__all__ = ("NewThingSchema", "ProductInfoSchema")


class ProductInfoSchema(BaseModel):
    price: Optional[str] = None
    source: Optional[str] = None


class NewThingSchema(ProductInfoSchema):
    id: Optional[int] = Field(default_factory=int)
    name: str
    author: str
    url: Optional[str] = None
    issue: Optional[int] = None
