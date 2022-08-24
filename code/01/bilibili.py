#!/usr/bin/env python3
# coding:utf-8

import itertools
import logging
import math
import pathlib
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, TypeVar

import pandas as pd
import requests
import requests_html

# --------------------
# Prerequisites
# --------------------

# internal types
_T = TypeVar("_T")
APIData = Dict[str, _T]
Records = List[APIData]

# api or data url
VIDEO_API_URL = "https://api.bilibili.com/x/space/arc/search"
VIDEO_PAGE_URL = "https://www.bilibili.com/video/{bvid}"

# request header
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2)",
    "AppleWebKit/537.36 (KHTML, like Gecko)",
    "Chrome/81.0.4044.92",
    "Safari/537.36",
    "Edg/81.0.416.53",
]
HEADERS = {"User-Agent": " ".join(USER_AGENTS)}

MID_NUMBER = "533459953"
params = {"ps": "30", "tid": "0", "order": "pubdate"}


# logger
logging.basicConfig(
    level=logging.INFO,
    format="[{asctime}]-[{levelname:<8}]-[{funcName}:{lineno}] - {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    style="{",
)
log = logging.getLogger(__name__)


# -----------------------
# Query and Handle Method
# -----------------------


def fetch_page_number(mid: str) -> int:
    """fetch total page number from API at first time query."""

    total = 0
    payloads = {"mid": mid, "pn": 1, **params}
    with requests.Session() as sess:
        response = sess.get(
            url=VIDEO_API_URL,
            headers=HEADERS,
            params=payloads,
        )
        response.raise_for_status()

        count = response.json()["data"]["page"]["count"]
        total += math.ceil(int(count) / 30)

    return total


def fetch_video_data(mid: str, page: int) -> List[APIData]:
    """fetch video data from API."""

    payload = {"mid": mid, "pn": str(page), **params}
    with requests.Session() as sess:
        response = sess.get(
            url=VIDEO_API_URL,
            headers=HEADERS,
            params=payload,
        )

        response.raise_for_status()

        jsons = response.json()["data"]["list"]["vlist"]
        log.info(f"fetch video from '{mid}' at {page} page.")
        return jsons


async def fetch_stats(bvid: str, asess) -> APIData:
    """fetch like, coin, collect and share from video page."""

    info = {}
    stats = ["rank", "like", "coin", "collect", "share"]
    response = await asess.get(
        url=VIDEO_PAGE_URL.format(bvid=bvid),
        headers=HEADERS,
    )
    response.raise_for_status()
    html = response.html

    has_rank = html.find(".video-data .rank", first=True)
    if has_rank:
        info["rank"] = has_rank.text.strip()

    try:
        info["like"] = html.find(".toolbar-left .like", first=True).text.strip()
        info["coin"] = html.find(".toolbar-left .coin", first=True).text.strip()
        info["collect"] = html.find(".toolbar-left .collect", first=True).text.strip()
        info["share"] = html.find(".toolbar-left .share", first=True).text.strip()
    except AttributeError:
        log.warning(f"cant' get stats from '{bvid}', use default.")
        return {k: "" for k in stats}

    log.info(f"fetch stats from '{bvid}'.")
    return info


async def bundle(json, asess) -> APIData:
    """bundle json data with stats."""

    bvid = json["bvid"]
    stats = await fetch_stats(bvid, asess)
    info = {**json, **stats}
    return info


def query(mid: str) -> Records:
    """query data by mid number."""

    log.info(f"querying data from '{mid}'...")

    total_page = fetch_page_number(mid)
    with ThreadPoolExecutor(max_workers=2) as p:
        features = [
            p.submit(fetch_video_data, mid=mid, page=page)
            for page in range(1, total_page + 1)
        ]
        jsons = itertools.chain(*[f.result() for f in features])

    # async session for html request
    asess = requests_html.AsyncHTMLSession(workers=2)

    # compatible with requests-html async coroutine codes
    # see: https://github.com/psf/requests-html/issues/362
    results = asess.run(
        *[lambda json=json, asess=asess: bundle(json, asess) for json in jsons]
    )
    return results


def parse(jsons: Records) -> pd.DataFrame:
    """normalize and combine json data."""

    return pd.json_normalize(jsons)


def main():
    csvfile = pathlib.Path("~/Desktop/bilibili.csv").expanduser()

    jsons = query(MID_NUMBER)
    data = parse(jsons)
    data.to_csv(csvfile, index=False)


if __name__ == "__main__":
    main()
