l = []
def trinity(n):
    s = ""
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s
for n in range(10000):
    x = trinity(n)
    summ = x.count("1") + (x.count("2") * 2)
    if summ % 3 == 0:
        x = "112" + x[2:]
    else:
        x += trinity(summ)
    R = int(x, 3)
    if R % 2 == 0 and R < 679:
        l.append(R)
print(max(l))