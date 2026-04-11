from itertools import *
word = "ШКОЛА"
k = 0
for i in product(word, repeat= 3):
    if i.count("К") == 1:
        k += 1
print(k)