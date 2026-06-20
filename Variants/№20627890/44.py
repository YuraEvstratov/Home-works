n = (9 ** 8) * (3 ** 20) - 3 ** 10 - 3
s = ""
while n != 0:
    s = str(n % 3) + s
    n //= 3
print(s.count("2"))