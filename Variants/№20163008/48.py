from sys import*
setrecursionlimit(10 ** 8)
def f(n):
    if n >= 25:
        return f(n - 5) + 5580
    else:
        return 12 * (g(n - 11) - 14)

def g(n):
    if n >= 395881:
        return n / 6 + 34
    else:
        return 13 + g(n + 39)
    
print(f(937))