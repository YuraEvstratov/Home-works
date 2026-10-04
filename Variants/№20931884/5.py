from itertools import *
matrix = "234 136 12 157 467 25 45".split()
graf = "FB BD DA AE EC CG GF FD GE".split()
print("1 2 3 4 5 6 7")
for i in permutations("FBDAECG"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break