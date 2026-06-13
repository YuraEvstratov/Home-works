from itertools import *
matrix = "578 478 457 237 136 58 1234 126".split()
graf = "АБ БВ ВИ ИЖ ЖЕ ЕА АГ ГБ ГЕ ВД ДЖ".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЖИ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break