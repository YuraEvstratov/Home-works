from sys import *
setrecursionlimit(10**8)
def f(n):
    if n > 1000000:
        return n
    else:
        return n + f(2 * n)
g = f(1000)/1000
count = 0
print(len([1 for i in range(1, 2000) if (f(i)/ i) == g]))