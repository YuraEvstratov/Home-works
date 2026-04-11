from itertools import *
k = 0
word = "МУЖЧИНА"
chet = 0
for i in permutations(word, 6):
    if i[0] != "Ч" and i.count("Ж") >= 1:
        chet += 1
        if chet % 2 != 0:
            k += 1
print(k)

