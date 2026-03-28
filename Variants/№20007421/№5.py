l = []
for n in range(1,1000):
    x = bin(n)[2:]
    if n % 2 == 0:
        x = "10" + x + "0"
    else:
        x = x + bin(x.count("1"))[2:]
    R = int(x, 2)
    if R > 600:
        l.append(n)

print((l))
# ОТВЕТ НЕ ВЕРНЫЙ