l = []
for n in range(100):
    x = bin(n)[2:]
    x = x[::-1]
    R = int(x, 2)
    if R == 13:
        l.append(n)
print(max(l))