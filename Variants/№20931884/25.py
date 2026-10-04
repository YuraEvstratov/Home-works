from itertools import *
word = "ЛЕВИЙ"
k = 0
for i in permutations(word):
    if i[0] != "Й" and "ЕИ" not in i:
        k += 1
print(k)
