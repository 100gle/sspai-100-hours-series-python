from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    n = [1, 3, 5, 10, 20]

    with ProcessPoolExecutor(max_workers=4) as pool:
        result = pool.map(fib, n)
        print(list(result))


if __name__ == '__main__':
    main()
