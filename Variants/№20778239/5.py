from itertools import *
matrix = "346 57 14 137 267 15 245".split()
graf = "АБ БВ ВГ ГЖ ЖЕ ЕД ДА БД ГЕ".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break
    