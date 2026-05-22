from itertools import *
matrix = "2389 1356 127 69 267 1459 35 19 1468".split()
graf = "АБ БВ ВЕ ЕК КИ ИЖ ЖГ ГА БГ БЕ ГД ДЕ ДЖ ДК".split()
print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break 