from itertools import *

matrix = "23679 14569 167 29 26 1235 138 79 1248".split()
grath = "АБ БВ ВЕ ЕК КИ ИЖ ЖГ ГА ГБ ГИ ГД БД ДИ ДЕ ДВ".split()

print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in grath):
        print(*i)
        break