l = []
def trinity(n):
    s = ""
    while n != 0:
        s = str(n % 3) + s
        n = n // 3
    return s
for n in range(100000000, 0, -1):
    x = trinity(n)
    q = ""
    for i in range(len(x)):
        if x[i] == "0":
            q += "2"
        elif x[i] == "2":
            q += "0"
        elif x[i] == "1":
            q += "1"
    z = int(q, 3)
    R = abs(n - z)
    if R == 1864246:
        l.append(n)
        break
print(min(l))
