from itertools import *

matrix = "34678 36 1267 1569 48 12349 138 157 46".split()
grath = "АБ БВ АГ ГБ БД ДВ ВЕ ГД ДЕ ГЖ ГИ ДИ ЕК ЖИ ИК".split()

print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in grath):
        print(*i)
        break
#ДАБИКГВЕЖ