from itertools import *

graf = "FC CG GA AD DB BF CE FE GE BE".split()
marix = "47 357 2567 16 236 345 123".split()
print("1 2 3 4 5 6 7")
for i in permutations("ABCDEFG"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break