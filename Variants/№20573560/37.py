from sys import *
setrecursionlimit(10 ** 8)
def f(n):
    if n <= 7:
        return n
    return g(n - 3) * 3
def g(n):
    if n <= 7:
        return n
    return g(n - 1) + 4
print(f(43000))