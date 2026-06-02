from itertools import *
words = "ABCDX"
k = 0 
for i in product(words, repeat= 4):
    if i.count("X") == 1:
        k += 1
print(k)