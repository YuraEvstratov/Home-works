from itertools import *

graf = "АБ БД ДЕ ЕК КГ ГВ ВА БВ ВД ВЕ ЕГ".split()
marix = "24 146 567 1267 36 23457 346".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break