from itertools import *
matrix = "246 13457 257 1267 23 147 2346".split()
graf = "АВ ВЕ ЕК КГ ГБ БА АГ ВГ ВД ЕД КД ГД".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break