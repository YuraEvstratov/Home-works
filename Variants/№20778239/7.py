def trin(n):
    z = ""
    while n != 0:
        z = str(n % 3) + z
        n //= 3
    return z
l = []
for n in range(100000):
    x = trin(n)
    if (x.count("1") + x.count("2") * 2) % 3 == 0:
        x = "112" + x[3:]
    else:
        x += trin(x.count("1") + x.count("2") * 2)
    R = int(x, 3)
    if R % 2 == 0 and R > 702:
        l.append(R)
print(min(l))
