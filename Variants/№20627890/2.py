from itertools import *
matrix = "37 57 147 37 26 57 12346".split()
graf = "AC AD AG DB DE BF EF".split()
print("1 2 3 4 5 6 7")
for i in permutations("ABCDEFG"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break