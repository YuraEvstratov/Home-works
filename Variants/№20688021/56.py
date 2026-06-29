from sys import *
setrecursionlimit(10 ** 8)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n - 2 + f(n - 1)
print(f(2023) - f(2021))