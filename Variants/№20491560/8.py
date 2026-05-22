from itertools import *
matrix = "24567 146 5 12 1367 125 15".split()
graf = "АБ БВ БЖ БЕ ВЖ ЕЖ ЕД ЖГ ЖД ГД ".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break 