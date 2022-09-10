from typing import TypeVar, Union

Number = TypeVar("Number", bound=Union[int, float])


def divide(x: Number, y: Number) -> Number:
    result = x / y
    return result


def main():
    print(divide(2, 1))
    print(divide(0, 1))
    print(divide(100, 10))


if __name__ == '__main__':
    main()
