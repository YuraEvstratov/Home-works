from itertools import *
matrix = "34678 36 1267 1569 48 12349 138 157 46".split()
graf = "АБ БВ ВЕ ЕК КИ ИЖ ЖГ ГА БГ БД ВД ГД ДЕ ГИ ДИ".split()
print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break