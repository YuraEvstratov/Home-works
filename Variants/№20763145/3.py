from itertools import *
matrix = "24 146 45 12356 34 24".split()
graf = "DC DB DE CB EB BA BG AG".split()
print("1 2 3 4 5 6")
for i in permutations("ABCDEG"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break