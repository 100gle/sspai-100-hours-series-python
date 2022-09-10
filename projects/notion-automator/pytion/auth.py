from pydantic import BaseModel, validator
from pytion import _types

__all__ = "AuthorizationHeader"


class AuthorizationHeader(BaseModel):
    authorization: str
    notion_version: str = "2022-06-28"
    content_type: str = "application/json"
    accept: str = "application/json"

    @validator("authorization")
    def has_bearer_prefix(cls, value: str) -> str:
        return f"Bearer {value}" if not value.startswith("Bearer") else value

    def dict(self, **kwargs) -> _types.DictLike:
        data = super(AuthorizationHeader, self).dict(**kwargs)
        headers = {}
        for key in data.keys():
            new = "-".join([part.capitalize() for part in key.split("_")])
            headers[new] = data[key]
        return headers
