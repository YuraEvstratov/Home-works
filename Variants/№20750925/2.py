from itertools import *
graf = "АБ БГ ГД ДЕ ДВ ВА БВ ГВ".split()
matrix = "3456 6 15 156 134 124".split()
print("1 2 3 4 5 6")
for i in permutations("АБВГДЕ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break
    