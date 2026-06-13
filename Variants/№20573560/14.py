l = []
def trinity(n):
    s = ""
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s
for n in range(1000000):
    x = trinity(n)
    if n % 3 == 0:
        x = "1" + x + "02"
    else:
        x = trinity((n % 3) * 4) + x
    R = int(x, 3)
    if R > 135:
        l.append(n)
print(min(l))