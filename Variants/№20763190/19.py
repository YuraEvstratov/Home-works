num = 3 * 125 ** 6 + 2 * 25 ** 9 + 5 ** 12 - 625
def f(n):
    s = ""
    while n != 0:
        s = str(n % 5) + s
        n //= 5
    return s
print(f(num).count("0"))
