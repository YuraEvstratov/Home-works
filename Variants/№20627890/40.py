n = 343 ** 5 - 7 ** 9 + 48
s = "" 
while n != 0:
    s = str(n % 7) + s
    n //= 7
print(s.count("6"))