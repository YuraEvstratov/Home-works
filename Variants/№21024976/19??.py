from itertools import *
k = 0
nums = "0123456789XXXXX"
for i in product(nums, repeat= 8):
    if i[0] != "0" and i.count("0") == 2 and i.count("X") <= 4:
        k += 1
print(k)
