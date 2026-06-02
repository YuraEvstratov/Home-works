from sys import *
setrecursionlimit(10 ** 8)
def f(n):
    if n % 2 == 0:
        return f(n // 2) + 3
    if n % 3 == 0:
        return f(n // 3) + 2
    return 0
n = 1
while True:
    if f(n) == 67:
        print(n)
        break
    n += 1