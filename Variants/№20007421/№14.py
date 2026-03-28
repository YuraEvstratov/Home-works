from itertools import *
word = "УЧЕНИК"
k = 0
for i in product(word, repeat=5):
    if i[0] == "У" and i[-1] == "К":
        k += 1
print(k)
