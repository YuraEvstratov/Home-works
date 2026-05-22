def f(i, m):
    if i >= 108:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i + 1, m - 1),
         f(i * 2, m - 1),
         f(i * 1.5, m - 1)]
    w = [f(i + 1, m - 1),
         f(i * 1.5, m - 1)]
    if i % 2 != 0:
        return any(h) if (m + 1) % 2 == 0 else all(h) 
    return any(w) if (m + 1) % 2 == 0 else all(w) 
print("19:", min([i for i in range(1, 108) if f(i, 2)]))
print("20:", *[i for i in range(1, 108) if f(i, 3) and not(f(i, 1))])
print("21:", min([i for i in range(1, 108) if f(i, 4) and not(f(i, 2))]))