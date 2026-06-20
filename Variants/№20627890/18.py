from itertools import *
nums = "0123456789xxxxx"
k = 0
for i in product(nums, repeat= 8):
    if i[0] != "0" and i.count("0") == 2 and i.count("x") < 5:
        k += 1
print(k)