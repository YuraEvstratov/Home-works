from itertools import *
word = "ЗИМА"
k = 0
for i in product(word,repeat= 5):
    if (i[0] == "З" or i[0] == "М") and (i[-1] == "И" or i[-1] == "А"):
        k += 1
print(k)