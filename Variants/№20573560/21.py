from itertools import *
word = "ТИМОФЕЙ"
k = 0
for i in product(word, repeat= 5):
    if i.count("Т") >= 1 and i.count("Й") <= 1:
        k += 1
print(k)