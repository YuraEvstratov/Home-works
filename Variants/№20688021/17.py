l = []
def trinity(n):
    s = ""
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s
for n in range(2, 10000):
    x = trinity(n)
    z = 0
    if n % 3 == 0:
        x = x + x[-2] + x[-1]
    else:
        for i in range(len(x)):
            z += int(x[i])
        x += trinity(z * 3)
    R = int(x, 3)
    if R >800 and R < 850:
        l.append(R)
print(l)