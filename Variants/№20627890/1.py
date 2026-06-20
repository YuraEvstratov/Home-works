from itertools import *
matrix = "6 6 456 35 3467 1235 5".split()
graf = "АВ ДВ ВБ ВГ БГ БЖ ГЕ".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break