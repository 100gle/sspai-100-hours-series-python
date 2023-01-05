import sys
from typing import Tuple, TypeVar

import pytest

Number = TypeVar("Number", int, float)
VERSION = "0.0.2"


def accumulate(*numbers: Tuple[Number]) -> Number:
    result = 0
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError(f"{n} isn't a valid number value")

        result += n

    return result


@pytest.mark.xfail()
@pytest.mark.parametrize("numbers, expected", argvalues=[([10, 11, -11, -12], 1)])
def test_accumulate_with_failed(numbers, expected):
    assert accumulate(*numbers) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    argvalues=[
        pytest.param(
            [10, 11, -11, -12], 1, marks=pytest.mark.xfail(reason="expected failed")
        )
    ],
)
def test_accumulate_with_failed_mark(numbers, expected):
    assert accumulate(*numbers) == expected


@pytest.mark.skip(reason="the case is WIP")
def test_wip_with_skip_mark():
    ...


def test_wip_with_skip_function():
    if VERSION <= '0.0.2':
        pytest.skip("the API is still on WIP")
    assert False


@pytest.mark.skipif(sys.platform != "linux", reason="only for linux")
def test_wip_function_only_for_linux():
    assert True
