l = []
def f(n):
    z = 0
    while n != 0:
        z += n % 10
        n //= 10
    return z
for n in range(10000):
    x = bin(n)[2:]
    if f(n) % 2 != 0:
        x += "1"
    else:
        x += "0"
    if f(int(x, 2)) % 2 != 0:
        x += "1"
    else:
        x += "0"
    if f(int(x, 2)) % 2 != 0:
        x += "1"
    else:
        x += "0"
    R = int(x, 2)
    if R > 1028:
        l.append(R)
print(min(l))
        