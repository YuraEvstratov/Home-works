l = []
for n in range(1, 10000):
    x = bin(n)[2:]
    x += str(x.count("1") % 2)
    x += str(x.count("1") % 2)
    R = int(x, 2)
    if R > 170:
        l.append(n)
print(min(l))
