from itertools import *
matrix = "345 457 167 1256 124 347 236".split()
graf = "АВ ВЕ ВГ АГ ЕД ГД ДБ ДЖ ЕЖ БЖ АБ".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break 