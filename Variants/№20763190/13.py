def f(n):
    s = ""
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s
num = (9 ** 8) * 3 ** 20 - 3 ** 10 - 3
x = f(num)
print(x.count("2"))