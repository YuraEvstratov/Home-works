from itertools import *
word = "КОТ"
k = 0
for i in product(word, repeat= 6):
    if i.count("К") == 1:
        k += 1
print(k)
