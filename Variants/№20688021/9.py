from itertools import *

graf = "АБ БГ ГЕ ЕЗ ЗЖ ЖД ДГ ГВ ВА АГ ГЗ ГЖ".split()
marix = "235 13 1245678 36 13 347 368 37".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЗЖ"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break