l = []
for n in range(10000):
    x = bin(n)[2:]
    x += str(x.count("1") % 2)
    x += str(x.count("1") % 2)
    R = int(x, 2)
    if R > 93:
        l.append(R)
print(min(l))
