from itertools import *
num = "012345678" 
k = 0
for i in product(num, repeat=6):
    if i[0] != "0" and i[0] != "1" and i[0] != "3" and i[0] != "5" and i[0] != "7" and i[-1] != "2" and i[-1] != "3" and i.count("1") >= 2:
        k += 1
print(k) 