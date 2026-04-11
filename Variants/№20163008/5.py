from itertools import *

matrix = "256 15 4 356 1246 145".split()
graf = "АБ БГ ГД ДЕ ДВ ВА БВ ВГ".split()

print("1 2 3 4 5 6")
for i in permutations("АБВГДЕ"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in graf):
        print(*i)
        break