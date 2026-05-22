from itertools import *
matrix = "56 3478 247 23 168 1578 2368 2567".split()
graf = "АБ ЕА ЕГ АГ ГБ ГЖ БЖ БД ЖД ЖИ ДИ ДВ ВИ".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЖИ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break 