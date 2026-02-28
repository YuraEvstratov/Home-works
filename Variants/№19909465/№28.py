from functools import *
from sys import *
setrecursionlimit(10 ** 100)
@lru_cache()
def f(n):
    if n <= 7:
        return n
    return g(n - 3) * 3

setrecursionlimit(10 ** 100)
@lru_cache()
def g(n):
    if n <= 7:
        return n
    return g(n - 1) + 4
print(f(43000))
# не решил