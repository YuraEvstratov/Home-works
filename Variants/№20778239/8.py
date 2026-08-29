l = []
for i in range(100000):
    x = bin(i)[2:]
    x += str(x.count("1") % 2)
    x += str(x.count("1") % 2)
    R = int(x, 2)
    if R > 97:
        l.append(R)
print(min(l))
