from sys import *
setrecursionlimit(10**8)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n // 10) + n % 10
    return f(n // 10)
l = []
for i in range(10**8):
    if 10 ** 7 <= f(i) <= 6 * 10 ** 7:
        l.append(i) 
print(len(l))
# не решил