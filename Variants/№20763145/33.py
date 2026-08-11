from itertools import *
nums = "0123456789"
k = 0
for i in permutations(nums, 6):
    x = "".join(i)
    if x[0] != "0" and (x[-1] == "0" or x[-1] == "5"):
        if int(x[0]) % 2 != int(x[1]) % 2 and int(x[1]) % 2 != int(x[2]) % 2 and int(x[2]) % 2 != int(x[3]) % 2 and int(x[3]) % 2 != int(x[4]) % 2 and int(x[4]) % 2 != int(x[5]) % 2:
            k += 1
print(k)
