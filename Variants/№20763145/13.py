l = []
for n in range(256):
    x = bin(n)[2:]
    if len(x) < 8:
        x = '0' * (8 - len(x)) + x
    x = x.replace('1', '*')
    x = x.replace('0', '1')
    x = x.replace('*', '0')   
    R = int(x, 2)
    if R - n == 111:
        print(n)