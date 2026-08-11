from itertools import *
matrix = "27 1567 67 5 246 2357 1236".split()
graf = "АБ БД БВ ДВ ДК КЕ ЕГ ГВ ВЕ ДЕ".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break