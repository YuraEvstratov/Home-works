from itertools import *
word = "ОЛЬГА"
k = 0
for i in permutations(word):
    if i[0] != "Ь" and i[i.index("A") + 1] != "Ь" or i[i.index("О") + 1] != "Ь":
        k += 1


# НЕ РЕШЕНО