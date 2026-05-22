from itertools import*
k = 0
num = "0123456"
for i in product(num, repeat= 4):
    if i[0] != 0 and i[0] > i[1] > i[2] > i[3]:
        k += 1
print(k) 