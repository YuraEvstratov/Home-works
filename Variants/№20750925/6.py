l = []
for n in range(100000):
    x = bin(n)[2:]
    b = str()
    for i in range(len(x)):
        if x[i] == "1":
            b += "0"
        else:
            b += "1"
    b = str(int(b))
    R = int(b, 2) 
    if n - R == 999:
        l.append(n)
print(min(l))
    