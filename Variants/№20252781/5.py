from itertools import *

matrix = ("24 146 567 1267 36 23457 346").split()
grath = ("АБ БД ДЕ ЕК КГ ГВ ВА БВ ВД ВЕ ЕГ").split()

print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in grath):
        print(*i)
        break