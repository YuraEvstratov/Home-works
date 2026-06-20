from itertools import *
matrix = "67 356 247 35 246 125 13".split()
graf = "BD DE EA AC CG GB GF CF FE".split()
print("1 2 3 4 5 6 7")
for i in permutations("ABCDEFG"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break