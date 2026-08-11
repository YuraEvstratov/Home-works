from itertools import product
k = 0
nums = "0123456"
for i in product(nums, repeat= 4):
    x = "".join(i)
    if x[0] != "0" and int(x[0]) > int(x[1]) > int(x[2]) > int(x[3]):
        k += 1
print(k)
