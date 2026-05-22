l = []
for n in range(1, 10000):
    x = bin(n)[2:]
    if n % 2 == 0:
        x = "10" + x
    else:
        x = "1" + x + "01"
    R = int(x, 2)
    if R > 516:
        l.append(n)
print(min(l))