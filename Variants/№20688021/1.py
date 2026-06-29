from itertools import *

graf = "BH HF FD DC CE EA AB AH EG GF CG".split()
marix = "247 148 578 126 38 47 236 235".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("ABCDEFGH"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)