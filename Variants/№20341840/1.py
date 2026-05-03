from itertools import *

graf = "ДЕ ЕК КА АБ БВ ВГ ГД ДВ КБ".split()
matrix = "67 346 24 235 47 127 156".split()

print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break