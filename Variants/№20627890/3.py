from itertools import *
matrix = "249 17 456 1369 38 3478 268 567 14".split()
graf = "АБ БВ ВЕ ЕК КИ ИЖ ЖГ ГА АД ДЖ БД ДИ ИЕ".split()
print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break