import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

__all__ = "settings"


class Settings(BaseSettings):

    NOTION_TOKEN: str = os.getenv("NOTION_TOKEN", "")
    NOTION_DATABASE_ID: str = os.getenv("NOTION_DATABASE_ID", "")

    PYTION_DEBUG: int = os.getenv("PYTION_DEBUG", 20)
    PYTION_LOG_FORMAT: str = "[{asctime}] [{levelname}] [{module}] - {message}"


settings = Settings()
