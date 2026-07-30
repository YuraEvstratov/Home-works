from itertools import *
graf = "АБ БИ ИЖ ЖА АВ АГ ЖГ ЖЕ ИЕ ИД БВ БД ВД ГЕ".split()
matrix = "3458 678 1457 1367 138 2478 2346 1256".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЖИ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break
    