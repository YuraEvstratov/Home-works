l = []
for n in range(1, 10000):
    x = bin(n)[2:]
    g = bin(n // 5)[2:]
    if n % 5 == 0:
        x += "11"
    else:
        x += g
    R = int(x, 2)
    if R >= 783:
        l.append(n)
print(min(l))
