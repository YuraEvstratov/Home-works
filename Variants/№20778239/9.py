l = []
for n in range(100000):
    x = bin(n)[2:]
    if n % 2 == 0:
        x = "1" + x + "1"
    else:
        x = "1" + x + "10"
    R = int(x, 2)
    if R <= 65:
        l.append(R)
print(max(l))
