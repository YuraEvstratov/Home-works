from itertools import *
nums = "01234567"
k = 0
for i in permutations(nums, 5):
    x = "".join(i)
    if x[0]!='0' and x.count('1')==0 and int(x[0])%2 != int(x[1])%2 and int(x[1])%2 != int(x[2])%2 and int(x[2])%2 != int(x[3])%2 and int(x[3])%2 != int(x[4])%2:
        k += 1
print(k)
