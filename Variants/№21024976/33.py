l = []
s = "01234567"
for x in s:
    for y in s:
        rez = int(x + "01" + y + "4", 9) + int(x + y + "544", 8)
        if rez % 89 == 0:
            l.append(rez)
print(min(l) // 89)
