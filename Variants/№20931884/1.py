from itertools import *
matrix = "235 13 1245678 36 13 347 368 37".split()
graf = "АБ АВ БГ АГ ВГ ГЕ ЕЗ ГЗ ГД ДЖ ГЖ ЗЖ".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЗЖ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break