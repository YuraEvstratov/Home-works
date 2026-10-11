l = []
def f(n):
    z = "" 
    while n > 0:
        z = str(n % 3) + z
        n //= 3
    return z

for n in range(2,100000):
    x = f(n)
    if n % 3 != 0:
        x += f((n % 3) * 5)
    R = int(x, 3)
    if R > 146:
        l.append(n)
print(min(l))
