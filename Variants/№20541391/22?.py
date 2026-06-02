def f(i, m):
    if i >= 102:
        return m % 2 == 0
    if m == 0 or i % 3 == 0:
        return False
    h = [f(i + 1, m - 1),
         f(i + 2, m - 1),
         f(i * 2, m - 1)]
    return any(h) 
# if (m + 1) % 2 == 0 else all(h)
print("19", [i for i in range(1, 102) if f(i, 2) and i % 3 != 0])