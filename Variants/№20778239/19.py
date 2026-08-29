from itertools import *
k = 1
word = "АБРТЫ"
for x in product(word, repeat= 5):
    i = ''.join(x)
    if i.count("Ы") == 0 and i.count("АА") == 0:
        print(k)
        break
    k += 1
