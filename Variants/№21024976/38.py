import string 
l = []
s = "0123456789" + string.ascii_letters
for x in s[:12]:
    for y in s[:12]:
        f = int(y + "AA" + x, 12) + int(x + "02" + y, 14)
        if f % 80 == 0:
            l.append(f)
print(min(l) // 80)
