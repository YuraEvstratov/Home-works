for n in range(1, 100000):
    x = bin(n)[2:]
    x = x[:-1]
    if n % 2 != 0:
        x += "10"
    else:
        x += "01"
    R = int(x, 2)
    if R == 2018:
        print(n)
        break