from itertools import *
word = "ПОЛИНА"
glasn = "ОИА"
sogl = "ПЛН"
k = 0
for i in product(word, repeat= 4):
    if ((i[0] in glasn and i[1] in sogl and i[2] in glasn and i[3] in sogl) or 
        (i[0] in sogl and i[1] in glasn and i[2] in sogl and i[3] in glasn)):
        k += 1
print(k)