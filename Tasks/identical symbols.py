def intrsection(x: list, y: list) -> list:
    new_x = set(x)
    new_y = set(y)
    rezult = new_x & new_y
    new_rezult = list(rezult)
    return new_rezult

a = [1, 2, 3, 2, 4]
b = [2, 4, 6, 2]
print(intrsection(a, b))
