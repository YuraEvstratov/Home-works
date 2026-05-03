def f(i, m):
    if i > 67:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i + 1, m - 1),
         f(i + 4, m - 1),
         f(i * 5, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)

print("19:", min([i for i in range(1, 68) if f(i, 2)]))# почему any
print("20:", *[i for i in range(1, 68) if f(i, 3) and not f(i, 1)])
print("20:", min([i for i in range(1, 68) if f(i, 4) and not f(i, 2)]))