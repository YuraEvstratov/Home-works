l = []
for x in range(1, 7291):
    s = 27 ** 298 + 27 ** 269 - x
    k = 0
    while s:
        if s % 27 == 0:
            k + 1
        s //= 27
    l.append(k)

print(max(l))
