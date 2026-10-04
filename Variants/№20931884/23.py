from itertools import product
nums = "0123"
k = 0
for i in product(nums,repeat= 3):
    if i[0] != "0" and (int(i[0]) + int(i[2])) > int(i[1]):
        k += 1
print(k)
