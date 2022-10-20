import time
from concurrent.futures import ThreadPoolExecutor

import requests


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        usage = time.perf_counter() - start
        return usage

    return wrapper


def fetch(url, method="GET"):
    resp = requests.request(method=method, url=url)
    resp.raise_for_status()
    data = resp.json()
    return data


@timer
def hacking(urls, methods, workers=2):
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [
            pool.submit(fetch, url=url, method=method)
            for url, method in zip(urls, methods)
        ]
        _ = [future.result() for future in futures]


@timer
def normal(urls, methods):
    for url, method in zip(urls, methods):
        fetch(url=url, method=method)


def main():
    base = "https://httpbin.org/"
    methods = ["GET", "POST", "PATCH", "DELETE"]
    urls = [base + method.lower() for method in methods]

    normal_usage = normal(urls, methods)
    hacking_usage = hacking(urls, methods)

    print(f"normal usage: {normal_usage: .2f}s")
    print(f"hacking usage: {hacking_usage: .2f}s")


if __name__ == '__main__':
    main()
