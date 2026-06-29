def f(i, m):
    if i >= 103:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(i + 1, m - 1),
         f(i + 2, m - 1),
         f(i * 2, m - 1)]
    return any(h) 
print("19:", *[i for i in range(1,102) if f(i, 2) and i % 3 != 0])
# print("20:", *[i for i in range(1, 102) if f(i, 3) and not f(i, 1) and i % 3 != 0])
# print("21:", *[i for i in range(1, 102) if f(i, 4) and not f(i, 2) and i % 3 != 0])
