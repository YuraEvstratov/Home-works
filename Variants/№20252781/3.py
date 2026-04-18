from itertools import *

matrix = "278 17 47 356 4678 45 12358 157".split()
grath = "АБ БВ ВЕ ЕК КИ ИЖ ЖГ ГА АИ ГИ БИ БЕ ЕИ".split()

print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГЕЖИК"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in grath):
           print(*i)
           break
# НЕ ПОЛУЧИЛОСЬ