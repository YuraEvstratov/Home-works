l = []
def trinity(n):
    z = ""
    while n != 0:
        z = str(n % 3) + z
        n //= 3
    return z
for n in range(1864246, 10 ** 10):
    x = trinity(n)
    x.replace("0", "*")
    x.replace("2", "0")
    x.replace("*", "2")
    x = x.lstrip("0")
    R = int(x, 3)
    rez = abs(n - R)
    if rez == 1864246:
        l.append(n)
print(min(l))