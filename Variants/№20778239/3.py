from itertools import *
matrix = "2345678 15 16 157 124 138 14 16".split()
graf = "АБ БВ АД ВД БД ДГ ДЕ ГЖ ЕИ ЖИ ДЖ ДИ".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЖИ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break
    