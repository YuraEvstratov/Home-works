from itertools import * 
word = "МАНГУСТ"
k = 0
for i in product(word, repeat= 6):
    if i[0] != "А" and i.count("У") >= 1 and i.count("М") == 2:
        k += 1
print(k)
