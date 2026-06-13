l = []
for n in range(2, 1000000):
    x = bin(n)[2:]
    x += x[-2]
    x += x[1]
    R = int(x, 2)
    if R > 180:
        l.append(n)
print(min(l))