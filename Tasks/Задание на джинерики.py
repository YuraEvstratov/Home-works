from typing import TypeVar, List
from typeguard import typechecked

T = TypeVar("T", int, float)
@typechecked
def summ(l: List[T]) -> T:
    if not l:
        raise ValueError("Empty array")
    value = 0
    for i in range(len(l)):
        value += l[i]
    return value


try:
    print(summ([1, 2, 3]))
    print(summ([1, 2, 3, "abc"]))
except ValueError:
    print("Empty")
except TypeError:
    print("w")