class Proxy:
    def __init__(self, delegate):
        self.delegate = delegate

    def fetch(self):
        print(f"fetching {self.delegate.url} by proxy...")


class Request:
    def __init__(self, url, proxy=False):
        self.url = url
        self.proxy = Proxy(self) if proxy else None


if __name__ == "__main__":
    req = Request("https://sspai.com", proxy=True)
    req.proxy.fetch()
