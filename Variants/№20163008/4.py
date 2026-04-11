from itertools import *

matrix = "346 45 16 125 247 137 56".split()
graf = "DF FA AB BC CE EG GD DE CA".split()

print("1 2 3 4 5 6 7")
for i in permutations("ABCDEFG"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in graf):
        print(*i)
        break