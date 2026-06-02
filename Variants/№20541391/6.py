l = []
for n in range(1, 10000):
    x = bin(n)[2:]
    if n % 2 == 0:
        x += "00"
    else:
        x += "11"
    R = int(x, 2)
    if R < 94:
        l.append(n)
print(max(l))