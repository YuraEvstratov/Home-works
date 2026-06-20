from itertools import *
word = "ВИКОРТ"
k = 0
for i in permutations(word):
    k += 1
    if k == 265:
        print(i)