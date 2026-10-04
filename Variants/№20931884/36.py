def f(x, y):
    if x < y or x == 12 or x == 15:
        return 0
    if x == y:
        return 1
    s = 0
    s += f(x - 1, y)
    if x % 2 == 0:
        s += f(x // 2, y)
    if x % 3 == 0:
        s += f(x // 3, y)
    return s
print(f(19, 1))
