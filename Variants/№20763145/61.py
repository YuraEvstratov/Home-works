def f(i_1, i_2, m):
    if i_1 + i_2 >= 93:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i_1 + 1, i_2, m - 1),
         f(i_1, i_2 + 1, m - 1),
         f(i_1 * 2, i_2, m - 1),
         f(i_1, i_2 * 2, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)
print(min([i for i in range(1, 81) if f(12, i, 2)]))
print(*[i for i in range(1, 81) if f(12, i, 3) and not f(12, i, 1)])
print(max([i for i in range(1, 81) if f(12, i, 4) ]))