def f(x, y):
    if x < y or x == 10 or x == 15:
        return 0
    if x == y:
        return 1
    if x % 2 == 0 and x % 3 == 0 :
        return f(x - 1, y) + f(x // 2, y) + f(x // 3, y)
    if x % 2 == 0 and x % 3 != 0 :
        return f(x - 1, y) + f(x // 2, y)
    if x % 3 == 0 and x % 2 != 0:
        return f(x - 1, y) + f(x // 3, y)
    if x % 2 != 0 and x % 3 != 0:
        return f(x - 1, y)

print(f(22, 1))