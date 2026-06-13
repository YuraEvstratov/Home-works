l = []
for n in range(4, 100000):
    x = bin(n)[2:]
    if n % 3 == 0:
        x = x + x[-3] + x[-2] + x[-1]
    else:
        x += bin((n % 3) * 3)[2:]
    R = int(x, 2)
    if R < 100:
        l.append(n)
print(max(l))