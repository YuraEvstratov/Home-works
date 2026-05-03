from itertools import *

word = "СВЕТА"
k = 0
for i in product(word, repeat= 5):
    if i.count("С") >= 1:
        k += 1
print(k)