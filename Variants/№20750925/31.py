def f(n):
    if n > 1000000:
        return n
    return n + f(2 * n)

G = f(1000) / 1000
print(len([1 for i in range(1, 3001) if (f(i) / i) == G]))
