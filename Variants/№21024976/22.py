from itertools import *
nums = "0123456789ABCSSS"
k = 0
for z in product(nums, repeat= 6):
    i = ''.join(z)
    if i[0] != "0" and i.count("5") >= 1 and i.count("S") == 2 and "SS" in i:
        k += 1
print(k)
