import logging
import pathlib
import tempfile
from typing import Optional
from urllib.parse import parse_qs, urlparse

import requests

__all__ = "UnsplashClient"

# --------------
# Prerequisites
# --------------

API = "https://api.unsplash.com/photos/random"
LOG = logging.getLogger(__name__)
CACHED = pathlib.Path(tempfile.mkdtemp(prefix="pylash-"))


class APIQueryException(Exception):
    def __init__(self, status_code: int, detail) -> None:
        self.status_code = status_code
        self.detail = detail

    def __str__(self) -> str:
        return f"staus_code={self.status_code}, detail={self.detail}"


# ---------------------
# Unsplash Integration
# ---------------------


class UnsplashClient(object):
    def __init__(self, token: str) -> None:
        if not token:
            raise ValueError(f"UnsplashClient need a token for initialization.")
        self.token = token
        self._remaining = 50
        self._headers = {
            "Accept-Version": "v1",
            "Authorization": f"Client-ID {self.token}",
        }

    @property
    def remaining(self) -> int:
        return self._remaining

    def _download(self, url: str) -> pathlib.Path:
        """download image from target url"""

        # extract name from url query string.
        parser = urlparse(url)
        params = parse_qs(parser.query)

        name = params['ixid'][0]
        file = CACHED.joinpath(f"{name}.jpg")
        LOG.debug(f"save image to cached dir in: {file}")

        response = requests.get(url, stream=True, params=dict(w=1080, fm="jpg", q=80))
        total = 0
        with open(file, mode="wb") as f:
            for chunk in response.iter_content(1024):
                total += f.write(chunk)

        LOG.debug(f"writing data: {total >> 10} KB.")

        return file

    def fetch(self) -> Optional[pathlib.Path]:
        if self._remaining == 0:
            LOG.warning(
                "the API request/usage has exhausted."
                "Please try it after next hour time."
            )
            return

        response = requests.get(
            API, headers=self._headers, params={"orientation": "landscape"}
        )
        data = response.json()

        if response.status_code != 200:
            raise APIQueryException(status_code=response.status_code, detail=data)

        # this property is not thread safety.
        self._remaining = int(response.headers.get("X-Ratelimit-Remaining"))

        url = data["urls"].get("raw")
        image = self._download(url=url)
        return image


if __name__ == "__main__":
    from pylash import settings

    client = UnsplashClient(token=settings.TOKEN)
    client.fetch()
