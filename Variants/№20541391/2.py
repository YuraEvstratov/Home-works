from itertools import *
matrix = "58 35 256 57 1234678 35 458 157".split()
graf = "AB BC CD DA CA AE EF FG GH HA FA GA".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("ABCDEFGH"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break