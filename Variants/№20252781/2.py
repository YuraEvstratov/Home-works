from itertools import *

matrix = "256 159 468 367 127 134 45 39 28".split()
grath = "АБ БВ ВГ ГК КИ ИЖ ЖА АД ДЖ ДЕ ЕГ ЕК".split()

print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in grath):
         print(*i)
         break