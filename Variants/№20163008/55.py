def f(x, y):
    if x > y or x == 11:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x + 5, y)
print(f(1, 9) * f(9, 18))