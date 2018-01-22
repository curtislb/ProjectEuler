"""types.py

Custom type definitions for function and variable type-checking.
"""

__author__ = 'Curtis Belmonte'

from abc import ABCMeta, abstractmethod
from fractions import Fraction
from typing import Any, Generic, List, Optional, Sequence, Tuple, TypeVar, Union


# Generic type variables
T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)

# Custom type alias representing a real number
Real = Union[float, Fraction]

# Type representing a coordinate in a two-dimensional matrix
Coord = Tuple[Optional[int], int]


class Matrix(Sequence[List[T]], Generic[T]):
    """Type representing a two-dimensional matrix with mutable entries."""
    ...


class _Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __le__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __ge__(self, other: Any) -> bool:
        ...

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        ...


_CT = TypeVar('_CT', bound=_Comparable)

# Custom type variable for values that can be compared to each other
Comparable = Union[_CT, Any]
