def f(x, y):
    if x > 33:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 3, y)
print(f(3, 33))