l = []
def f(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s
for n in range(1000000):
    x = bin(n)[2:]
    if f(n) % 2 == 0:
        x += "0"
    else:
        x += "1"
    z = int(x, 2)
    if f(z) % 2 == 0:
        x += "0"
    else:
        x += "1"
    q = int(x, 2)
    if f(q) % 2 == 0:
        x += "0"
    else:
        x += "1"
    R = int(x, 2)
    if R > 2054:
        l.append(R)
print(min(l))