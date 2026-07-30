from itertools import *
word = "светлана"
k = 0
for i in permutations(word):
    x = ''.join(i)
    if "аа" not in x:
        k += 1
    print(x)
print(k)
