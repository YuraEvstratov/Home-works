from itertools import *
word = "АНДРЕЙ"
k = 0
for i in product(word, repeat= 6):
    if i.count("А") >= 1 and i.count("Й") <= 1:
        k += 1
print(k)