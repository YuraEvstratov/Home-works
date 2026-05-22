from itertools import *
matrix = "256 145 4 235 1246 15".split()
graf = "АБ БГ ГД ДЕ ДВ ВА БВ ВГ".split()
print("1 2 3 4 5 6")
for i in permutations("АБВГДЕ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break 