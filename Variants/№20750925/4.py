from itertools import *
graf = "АБ АВ БВ ВД ВЕ ВГ ДЕ ГЕ ЕК ГК".split()
matrix = "24 146 56 1267 36 23457 46".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break
    