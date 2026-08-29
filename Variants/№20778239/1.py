from itertools import *
matrix = "248 13 268 17 678 358 45 1356".split()
graf = "АБ БД ДК КЛ ЛЕ ЕВ ВА АГ БГ ДГ ЕГ".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕКЛ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)