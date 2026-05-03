from itertools import *
word = "ABCX"
k = 0
for i in product(word, repeat= 5):
    if i.count("X") == 1 and (i[0] == "X" or i[-1] == "X"):
        k += 1
print(k)