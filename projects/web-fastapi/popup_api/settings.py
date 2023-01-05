import pathlib

from pydantic import BaseSettings

APP_ROOT = pathlib.Path(__file__).parent


class Settings(BaseSettings):

    # fastapi settings
    VERSION = 0.1
    SITE_NAME = "Todolist - Popup"
    DESCRIPTION = """
    This is the brand new Todolist application,
    which built in FastAPI with RESTful APIs.
    """.strip()

    # database settings
    DATABASE_URL = f"sqlite:///{APP_ROOT / 'db.sqlite3'}"
    DATABASE_ECHO = True
    DATABASE_CONNECT_ARGS = {"check_same_thread": False}


settings = Settings()
