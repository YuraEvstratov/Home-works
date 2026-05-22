for n in range(10, 1000000000):
    x = bin(n)[2:]
    if n % 3 == 0:
        x += bin(n)[-3:]
    else:
        x += bin((n % 3)*3)[2:]
    R = int(x, 2)
    if R <= 137:
        print(R)
