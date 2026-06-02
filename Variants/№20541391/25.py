def f(i, m):
    if i >= 48:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i + 1, m - 1),
         f(i + 4, m - 1),
         f(i * 2, m - 1)]
    return any(h)
print("19", min([i for i in range(1, 48) if f(i, 2)]))