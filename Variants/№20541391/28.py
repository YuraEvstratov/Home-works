def f(i, m):
    if i > 19:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i - 1, m - 1),
         f(i // 3, m - 1),
         f(i - 2, m - 1)]
    
    e = [f(i - 1, m - 1),
         f(i // 5, m - 1),
         f(i - 3, m - 1)]
    if i % 3 == 0:
        return any(h)
    if i % 5 == 0:
        return any(e)

print("19", min([i for i in range(100, 1, -1) if f(i, 2)]))
