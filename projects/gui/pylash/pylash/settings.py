import os

from dotenv import load_dotenv

load_dotenv()


DEBUG = 10 if os.getenv("PYLASH_DEBUG") else False
TOKEN = os.getenv("PYLASH_TOKEN")

LOG_FORMAT = "[{asctime}] [{levelname}] [{name}] [{funcName}:{lineno}] - {message}"
