from itertools import *
nums = "012345678"
k = 0
er = ['12', '32', '52', '72', '21', '23', '25', '27']
for i in product(nums, repeat= 5):
    x = "".join(i)
    if x.count("3") == 2 and x[0] != "0" and all(not i in x for i in er):
        k += 1
print(k) 
