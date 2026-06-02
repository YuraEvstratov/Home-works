from itertools import *
matrix = "568 36 247 368 178 124 35 145".split()
graf = "БА АЖ ЖД ДК КЕ ЕБ БГ ГА ГВ ЕВ ВД".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЖК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break