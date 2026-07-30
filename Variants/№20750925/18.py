from itertools import *
word = "КОНФЕТА"
k = 0
for i in product(word, repeat= 5):
    x = ''.join(i)
    if x.count("Е") == 2 and x[1] != "Ф":
        k += 1
print(k)
        