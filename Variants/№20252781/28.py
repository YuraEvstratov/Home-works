from itertools import *
k = 0
word = "ABCDEFX"
for i in product(word, repeat= 4):
    if i.count("X") == 1:
        k += 1
print(k)