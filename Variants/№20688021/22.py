l = []
for n in range(10000):
    x = bin(n)[2:]
    if x.count("1") % 2 != 0:
        x += "11"
    else:
        x += "00"
    R = int(x, 2)
    if R > 114:
        l.append(R)
print(min(l))