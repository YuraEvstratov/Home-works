from itertools import *
graf = "GD DF FA AB BC CE EG ED AC".split()
matrix = "346 45 16 125 247 137 56".split()
print("1 2 3 4 5 6 7")
for i in permutations("ABCEFGD"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break