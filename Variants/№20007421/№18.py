from itertools import *
word = "012345"
k = 0
for i in product(word, repeat= 5):
    if i[0] != "0" and   i.count("5") >= 2 and i.count("1") + i.count("3") <= 3:
        k += 1
print(k)