from itertools import *
k = 0
word = "ГЕПАРД"
for i in product(word,repeat=5):
    if i.count("Г") == 1 and i[0] != "А" and i[-1] != "Е":
        k += 1
print(k)
