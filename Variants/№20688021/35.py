from itertools import *
num = "0123456789xxxxx"
k = 0
for i in product(num, repeat= 8):
    if i[0] != "0" and i.count("0") == 2 and i.count("x") <= 4:
        k += 1
print(k)
# считал 5 минут
