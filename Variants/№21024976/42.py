x = 9 ** 2016 + 3 ** 2015 - 9
s = '' 
while x != 0:
    s = str(x % 3) + s
    x //= 3
print(s.count("2"))