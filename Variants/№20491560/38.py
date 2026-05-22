from itertools import *
word = "МЕТРО"
k = 0
for i in product(word, repeat= 4):
    if (i[0] == "М" or i[0] == "Т" or i[0] == "Р") and (i[-1] == "Е" or i[-1] == "О"):
        k += 1
print(k)