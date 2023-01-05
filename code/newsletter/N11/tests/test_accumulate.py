from typing import Tuple, TypeVar

import pytest

Number = TypeVar("Number", int, float)


def accumulate(*numbers: Tuple[Number]) -> Number:
    result = 0
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError(f"{n} isn't a valid number value")

        result += n

    return result


def test_accumulate():
    numbers = [1, 2, 3, 4]
    expected = 10

    assert accumulate(*numbers) == expected


if __name__== '__main__':
    pytest.main()
