from itertools import *

matrix = "345 457 167 1256 124 347  236".split()
graf = "АБ БЖ ЖЕ ЕВ ВА АГ ВГ ГД ДЕ ДЖ ДБ".split()

print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in graf):
        print(*i)
        break
# НЕВЕРНЫЙ ОТВЕТ