l = []
def trinity(n):
    s = ""
    while n != 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]
for n in range(1, 10000):
    x = trinity(n)
    if n % 3 == 0:
        x = "1" + x + "02"
    else:
        x += trinity((n % 3) * 4)
    R = int(x, 3)
    if R <= 250:
        l.append(n)
print(max(l))
