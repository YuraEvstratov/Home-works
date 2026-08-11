l = []
def trinity(n):
    z = ""
    while n != 0:
        z = str(n % 3) + z
        n //= 3
    return z
for n in range(10000):
    x = trinity(n)
    if n % 3 == 0:
        x = "1" + x + "02"
    else:
        x += trinity((n % 3) * 4)
    R = int(x, 3)
    if R <= 250:
        l.append(n)
print(max(l))
