mx = otv = 0
for x in range(2030, 0, -1):
    num = 5 ** 150 + 5 ** 100 - x
    c = 0
    while num != 0:
        if num % 5 == 0:
            c += 1
        num //= 5
    if c >= mx:
        otv = x
        mx = max(mx, c)
print(otv)