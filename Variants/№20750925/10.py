l = set()
for n in range(10, 1001):
    x = bin(n)[3:]
    R = n - int(x, 2)
    if R not in l:
        l.add(R)
print(len(l))