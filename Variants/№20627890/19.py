from itertools import *
nums = "0123456789zzzxxx"
k = 0
for j in product(nums, repeat= 6):
    i = ''.join(j)
    if i.count("x") == 2 and i[0] != "0" and i.count("5") >= 1 and "xx" in i:
        k += 1
print(k)