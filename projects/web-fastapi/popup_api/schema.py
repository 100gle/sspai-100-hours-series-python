from typing import Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Response(BaseModel):
    code: int = 0
    message: str
    data: Optional[T]
