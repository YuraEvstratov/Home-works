from itertools import *
k = 0
word = "ЗИМА"
gl = "ИА"
sgl = "ЗМ"
for i in product(word, repeat= 5):
    if i[0] in sgl and i[-1] in gl:
        k += 1
print(k)
