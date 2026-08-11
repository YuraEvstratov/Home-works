def f(i, m):
    if i >= 65:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i + 1, m - 1),
         f(i * 4, m - 1)]
    return any(h) 
print(min([i for i in range(1, 65) if f(i, 2)]))
# print(*[i for i in range(1, 65) if f(i, 3) and not f(i, 1)])
# print(max([i for i in range(1, 65) if f(i, 4) and not f(i, 2)]))