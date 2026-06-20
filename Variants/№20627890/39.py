n = 125 ** 5 + 25 ** 9 - 30
s = ""
while n != 0:
    s = str(n % 5) + s
    n //= 5
print(s.count("4"))