l = []
def trinity(n):
    s = ""
    while n != 0:
        s += str(n % 3) 
        n = n // 3
    return s[::-1]
for n in range(1864648, 10000000):
    x = trinity(n)
    z = ""
    for i in range(len(x)):
        if x[i] == "2":
            z += "0"
        elif x[i] == "0":
            z += "2"
        elif x[i] == "1":
            z += "1"
    R = int(z, 3)
    if R == 1864648:
        l.append(n)
print(min(l))