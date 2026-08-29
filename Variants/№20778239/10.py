for n in range(100000):
    x = bin(n)[2:]
    if len(x) < 8:
        x = '0' * (8 - len(x)) + x
    x = x.replace('1', '*')
    x = x.replace('0', '1')
    x = x.replace('*', '0')
    R = int(x, 2) - n
    if R == 133:
        print(n)
