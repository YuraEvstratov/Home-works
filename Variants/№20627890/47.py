from sys import *
from functools import *
setrecursionlimit(10 ** 9)
@lru_cache(maxsize= 10 ** 8)
def f(n):
    if n == 0:
        return 0
    return f(n - 1) + n
l = []
for i in range(237567892, 1134567005):
    if f(i) % 3 == 0:
        l.append(i)
print(len(l))