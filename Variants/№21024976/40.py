import string
s = "0123456789"
l = []
for x in s:
    f = int("2AB" + x, 12) + int(x + "8E", 17)
    if f % 27 == 0:
        l.append(f)
print(min(l) // 27)
