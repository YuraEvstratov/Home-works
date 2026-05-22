from itertools import *
word = "НАСТЯ"
k = 0
for i in product(word, repeat= 6):
    if i.count("А") <= 1 and i.count("Я") <= 1:
        k += 1
print(k)