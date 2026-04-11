from itertools import *

matrix = "27 17 56 6 367 345 125".split()
grath = "ГА АД ДГ ДЕ ЕБ БВ БК КЕ".split()

print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in grath):
        print(*i)
        break