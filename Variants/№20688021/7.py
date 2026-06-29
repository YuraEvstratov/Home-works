from itertools import *

graf = "АБ БВ ВД ДЕ ЕК КИ ИЖ ЖГ ГА БД ГД ГИ ЕИ".split()
marix = "2567 17 4679 389 16 1358 123 46 34".split()
print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        