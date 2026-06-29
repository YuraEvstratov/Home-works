def f(i, m):
    if i <= 26005:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i - 2, m - 1),
         f(i - 7, m - 1),
         f(i // 3, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)
# print("19", max([i for i in range(80000, 26005, - 1) if f(i, 1)]))
print("20", *[i for i in range(80000, 26005, - 1) if f(i, 3) and not(f(i, 1))])
print("21", min([i for i in range(80000, 26005, - 1) if f(i, 4) and not(f(i, 2))]))

