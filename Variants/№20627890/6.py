l = []
for n in range(2, 10000):
    x = bin(n)[2:]
    x = x[:-1] + x[1] + x[1]
    R = int(x, 2)
    if R > 92:
        l.append(n)
print(min(l)) 