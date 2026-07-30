from itertools import *
nums = "0x2x4x6x8"
k = 0
for i in product(nums, repeat= 7):
    x = ''.join(i)
    if x.count("6") == 1 and x.count("x") == 2 and x[0] != "0":
        k += 1
print(k)
