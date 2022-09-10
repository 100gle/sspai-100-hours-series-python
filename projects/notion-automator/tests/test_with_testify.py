from typing import TypeVar, Union

Number = TypeVar("Number", bound=Union[int, float])


def divide(x: Number, y: Number) -> Number:
    result = x / y
    return result


def testify(func, *, expected, **kwargs):
    template = f"testing for {func.__name__} with {kwargs}..."
    result = func(**kwargs)
    if result == expected:
        print(template + "ok.")
        return True

    print(template + "failed.")
    return False


def main():
    cases = [
        testify(divide, x=2, y=1, expected=2),
        testify(divide, x=0, y=1, expected=0),
        testify(divide, x=100, y=10, expected=10),
        testify(divide, x=1, y=2, expected=2),
    ]
    is_passed = all(cases)
    print(is_passed)


if __name__ == '__main__':
    main()
