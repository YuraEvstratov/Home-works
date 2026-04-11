def f(x, y):
    if x < y or x == 10:
        return 0
    if x == y:
        return 1
    if x % 3 == 0:
        return f(x - 2, y) + f(x // 3, y)
    else:
        return f(x - 2, y) + f(x - 4, y)

print(f(38, 6))