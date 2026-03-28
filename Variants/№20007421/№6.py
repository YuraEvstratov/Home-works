l = []
def trinity(n):
    k = ""
    while n > 0:
        k = str(n % 3) + k
        n = n // 3
    return k
def summa(n):
    rez = 0
    while n > 0:
        rez += n % 10
        n = n // 10
    return rez
for n in range(10,1000):
    x = trinity(n)
    if n % 3 == 0:
        x = x + x[-2:]
    else:
        x = x +  trinity(summa(int(x)) * 3)
    R = int(x, 3)
    if 826 - 20 < R < 826 + 20:
        l.append(R)
print(l)