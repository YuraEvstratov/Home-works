from itertools import *
k = 0
word = "КАТЕР"
for i in product(word, repeat= 6):
    x = "".join(i)
    if x[0] == "Р" and x[-1] == "К":
        k += 1
print(k)