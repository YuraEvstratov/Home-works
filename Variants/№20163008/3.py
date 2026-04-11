from itertools import *

matrix = "6 356 2 5 247 12 5".split()
graf = "БВ АВ ВГ ГЖ ГЕ ЕД".split()

print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in graf):
        print(*i)
        break
    