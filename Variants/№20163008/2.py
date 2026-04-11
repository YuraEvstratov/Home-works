from itertools import *

graf = "BD DE EA AG GF FB BC DC CG".split()
matrix = "45 345 256 127 123 37 46".split()

print("1 2 3 4 5 6 7")
for i in permutations("ABCDEFG"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in graf):
        print(*i)
        break