def f(x, y, z, c):
    if x > y:
        return 0
    if x == y:
        return 1
    if z == False:
        return f(x * 2, y, True, False) + f(x * 3, y, True,False)
    if c == False:
        return f(x + 1, y, False, True) + f(x + 2, y, False, True)
    else:
        return f(x + 1, y, False, True) + f(x + 2, y, False, True) + f(x * 2, y, True, False) + f(x * 3, y, True,False)

print(f(1,24,True,True))