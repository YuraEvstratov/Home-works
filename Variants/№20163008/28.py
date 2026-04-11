from itertools import *
word = "0123456"
k = 0
for i in product(word, repeat= 5):
    if i[0] != "0" and (i[0] == "2" or i[0] == "4" or i[0] == "6") and (i[-1] == "2" or i[-1] == "3") and i.count("1") >= 2:
        k += 1
print(k)
