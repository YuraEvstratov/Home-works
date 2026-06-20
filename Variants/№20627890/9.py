l = []
def trinity(n):
    s = ""
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s
def summ(x):
    t = 0
    while x > 0:
        t += x % 10
        x //= 10
    return t
for n in range(1, 10000):
    x = trinity(n)
    if n % 3 == 0:
        x = x + x[-2:]
    else:
        x += trinity(summ(int(x)) * 3)
    R = int(x, 3)
    if 850 <= R <= 950:
        l.append(R)
print(l)