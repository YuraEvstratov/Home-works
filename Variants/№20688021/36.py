from itertools import *
k = 0
num = "0123456789"
for i in permutations(num, 4):
 if (int(i[0]) % 2 != int(i[1]) % 2) and (int(i[1]) % 2 != int(i[2]) % 2) and (int(i[2])  % 2 != int(i[3]) % 2) and i[0] != '0':
        k += 1
print(k)