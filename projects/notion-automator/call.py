import inspect
import sys
from pprint import pprint
from typing import Callable, Mapping, TypeVar, Union

if sys.version_info < (3, 10):
    from typing_extensions import ParamSpec
else:
    from typing import ParamSpec

T = TypeVar("T")
Number = TypeVar("Number", bound=Union[int, float])

Params = ParamSpec("Params")
Return = TypeVar("Return")
Func = Callable[Params, Return]


class FuncRegister:
    def __init__(self, module: str) -> None:
        self.module = module
        self._funcs = {}

    def __call__(self, func: Func, *args, **kwargs) -> Func:
        func_name = func.__name__
        func_docs = func.__doc__
        sig = inspect.signature(func)
        func_params = sig.parameters

        self._funcs[func_name] = dict(
            name=func_name,
            docs=func_docs,
            params=dict(func_params),
            return_type=sig.return_annotation,
        )

        return func

    def collect(self) -> Mapping[str, T]:
        return {self.module: self._funcs}


register = FuncRegister(__name__)


@register
def add(x: Number, y: Number) -> Number:
    """add operator for number"""
    return x + y


@register
def sub(x: Number, y: Number) -> Number:
    """sub operator for number"""
    return x - y


@register
def multiply(x: Number, y: Number) -> Number:
    """multiply operator for number"""
    return x * y


@register
def divide(x: Number, y: Number) -> Number:
    """divide operator for number"""
    return x / y


def main():

    funcs = register.collect()
    pprint(funcs)

    print(add(1, 1))
    print(sub(3, 1))
    print(multiply(3, 3))
    print(divide(100, 10))


if __name__ == "__main__":
    main()
