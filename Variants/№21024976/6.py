l = []
for n in range(2, 100000):
    x = bin(n)[2:]
    x += x[-2]
    x += x[2]
    R = int(x, 2)
    if R > 150:
        l.append(n)
print(min(l))
