from typing import Mapping, TypeVar, Union

__all__ = ["T", "DictLike", "PropertyLike", "Numeric"]

T = TypeVar("T")
DictLike = Mapping[T, T]
PropertyLike = DictLike
Numeric = TypeVar("Numeric", bound=Union[int, float])
