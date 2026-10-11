import string
a = "0123456789" + string.ascii_letters
for p in range(11, 36):
    for x in a[1:p]:
        for y in a[:p]:
            for z in a[1:p]:
                if int(z + x, p) + int(x + y, p) == int(z + y + "A", p):
                    print(int(x + y + z, p))
                    