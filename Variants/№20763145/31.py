from itertools import *
nums = "0123456789ABCsss"
k = 0
for i in product(nums, repeat= 6):
    x = "".join(i)
    if x[0] != "0" and x.count("5") >= 1 and x.count("s") == 2 and "ss" in x:
        k += 1
print(k)