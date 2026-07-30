l = []
for n in range(10000, 2 ** 29):
    x = bin(n)[2:]
    z = str(n)
    chet = 0
    nechet = 0
    for i in range(len(z)):
        if int(z[i]) % 2 == 0:
            chet += 1
        else:
            nechet += 1
    if chet > nechet:
        x += "1"
    if chet < nechet:
        x += "0"
    if chet == nechet:
        if n % 2 == 0:
            x += "0"
        else:
            x += "1"
    R = int(x, 2)
    if R > 876544 and R < 1234567899:
        l.append(R)
print(len(l))
