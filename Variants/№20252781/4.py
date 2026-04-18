from itertools import *

matrix = "23 145 16 27 267 357 456".split()
grath = ("CG GE EA AF FC FB BD DE DA").split()

print("1 2 3 4 5 6 7")
for i in permutations("FCGEABD"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in grath):
        print(*i)
        break