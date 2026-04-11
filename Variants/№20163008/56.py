def f(x, y, z):
    if x > y:
        return 0
    if x == y:
        return 1
    if z == "1":
        return f(x * 2, y, "2") + f(x * 3, y, "2")
    if z == "2":
        return f(x + 1, y , "1") + f(x + 2, y, "1")
    return f(x * 2, y, "2") + f(x * 3, y, "2") + f(x + 1, y , "1") + f(x + 2, y, "1")
print(f(1, 22, ""))