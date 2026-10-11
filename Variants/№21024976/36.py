import string
l = []
s = "0123456789" + string.ascii_letters
for x in s[:13]:
        s = int(x + "A04",13) + int("1D" + x + "3", 18)
        if s % 184 == 0:
                l.append(s)
print(min(l) // 184)
