num = 8 ** 2020 + 4 ** 2017 + 26 - 1
x = bin(num)[2:]
print(x.count("1"))