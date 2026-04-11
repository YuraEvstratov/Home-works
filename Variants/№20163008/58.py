def f(x, y, z):
    if x > y + 1:
        return 0
    if x == y:
        return 1
    if z == 1:
        return f(x + 3, y, 0) + f(x * 2, y, 0)
    return f(x - 1, y, 1) + f(x + 3, y, 0) + f(x * 2,y , 0)
print(f(3, 12, 0))
# ПОСМОТРЕЛ ОТВЕТ ТАК КАК ЗАПУТАЛСЯ