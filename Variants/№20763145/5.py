from itertools import *
matrix = "47 357 2567 16 236 345 123".split()
graf = "FC CG GA AD DB BF FE CE GE EB".split()
print("1 2 3 4 5 6 7")
for i in permutations("FCBEGAD"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break