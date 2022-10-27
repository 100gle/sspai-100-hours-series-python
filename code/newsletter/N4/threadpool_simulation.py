import contextlib


class Thread:
    def __init__(self, max_worker):
        self.max_worker = max_worker

    def execute(self, func, *args, **kwargs):
        print(f"Using {self.max_worker} workers to execute {func.__name__} function...")
        func(*args, **kwargs)


@contextlib.contextmanager
def ThreadPoolExecutor(max_worker=1):
    pool = Thread(max_worker)
    print("Initial for threads...")
    try:
        yield pool
    finally:
        print("Recycling threads and closing pool...")


def echo(s):
    print(f"\techo: {s}")


def main():
    with ThreadPoolExecutor(max_worker=2) as pool:
        pool.execute(echo, s="Hello, world!")


if __name__ == '__main__':
    main()
