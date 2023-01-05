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


def test_accumulate_without_mark():
    numbers = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [-1, 0, 1, 0],
        [10, 11, -11, -12],
    ]
    expected = (10, 26, 0, 1)

    for number, expect in zip(numbers, expected):
        assert accumulate(*number) == expect


@pytest.mark.parametrize(
    argnames="numbers,expected",
    argvalues=[
        ([1, 2, 3, 4], 10),
        ([5, 6, 7, 8], 26),
        ([-1, 0, 1, 0], 0),
        ([10, 11, -11, -12], 1),
    ],
    ids=list("abcd"),
)
def test_accumulate_with_parametrize_mark(numbers, expected):
    assert accumulate(*numbers) == expected


@pytest.mark.parametrize(argnames="even_number", argvalues=[2, 4])
@pytest.mark.parametrize(argnames="odd_number", argvalues=[1, 3])
def test_accumulate_with_multiple_parametrize_mark(even_number, odd_number):
    expected = {
        "1+2": 3,
        "1+4": 5,
        "3+2": 5,
        "3+4": 7,
    }
    expr = f"{odd_number}+{even_number}"
    assert accumulate(odd_number, even_number) == expected[expr]
