l = []
def f(n):
    s = 0
    while n:
        s *= n % 10
        n //= 10
    return s
def sm(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
for n in range(10000000):
    p = f(n)
    m = sm(p)
    T_1 = p + m
    T_2 = p * m
    R = str(T_1) + str(T_2)
    if R == "23126":
        l.append(n)
print(max(l))
