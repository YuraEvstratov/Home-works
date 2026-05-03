from itertools import *

words = "0234567"
k = 0
for i in product(words, repeat= 5):
    if int(i[0]) % 2 == 0:
        if int(i[2]) % 2 == 0:
            if int(i[4]) % 2 == 0:
                k += 1
    if int(i[0]) % 2 != 0:
        if int(i[2]) % 2 != 0:
            if int(i[4]) % 2 != 0:
                k += 1
print(k)