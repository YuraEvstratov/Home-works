from itertools import *

graf = "АБ БВ ВЕ ЕК КИ ИЖ ЖГ ГА ВГ ГД ДЕ ЕЖ".split()
marix = "2459 16 4579 138 136 25 38 47 13".split()
print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break