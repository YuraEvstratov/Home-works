maxe = 0
rez = 0
for n in range(10000):
    x = bin(n)[2:]
    if x.count("1") % 2 == 0:
        x ="1" + x[2:] + "0"
    else:
        x += "1"
        x = "11" + x[2:]
    R = int(x, 2)
    if R < 744:
        maxe =  max(maxe, R)
        if maxe == R:
            rez = n
print(rez)