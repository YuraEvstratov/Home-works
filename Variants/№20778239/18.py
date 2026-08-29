from itertools import *
word = "ПОЛИНА"
k = 0
for i in product(word, repeat= 8):
    if (i.count("П") + i.count("Л") + i.count("Н")) > (i.count("О") + i.count("И") + i.count("А")):
        k += 1
print(k)
