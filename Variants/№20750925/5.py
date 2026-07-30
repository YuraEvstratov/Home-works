from itertools import *
graf = "АБ БВ ВК КИ ИА АВ АГ ИЕ ЖК ГД ДЖ ЖЕ ЕГ".split()
matrix = "49 57 789 156 2478 489 235 356 136".split()
print("1 2 3 4 5 6 7 8 9")
for i in permutations("АБВГДЕЖИК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break
    