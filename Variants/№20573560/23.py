from itertools import *
word = "ПЯТНИЦА"
k = 0
for i in product(word, repeat= 5):
    if i[0] != "Н" and i.count("Я") == 1:
        k += 1
print(k)