from itertools import *
word = "ВОЛК"
k = 0
for i in product(word, repeat= 5):
    x = "".join(i)
    if x.count("В") == 1:
        k += 1
print(k)