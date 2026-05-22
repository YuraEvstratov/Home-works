from itertools import *
word = "0123456789Axxx"
k = 0
for q in product(word, repeat= 6):
    i = ''.join(q)
    if i[0] != "0" and i.count("4") >= 1 and i.count("x") == 2 and "xx" in i:
        k += 1
print(k)