l = []
def trinity(n):
    z = ""
    while n > 0:
        z = str(n % 3) + z
        n //= 3
    return z
def summ(n):
    rezult = 0
    while n > 0:
        rezult += n % 10
        n //= 10
    return rezult

for n in range(3, 1000):
    x = trinity(n)
    if n % 3 == 0:
        x = x + x[-2:]
    else:
        x = x + trinity(summ(int(n)) * 3)
    R = int(str(x), 3)
    if 860 <= R <= 960:
        l.append(R)
print(l)


