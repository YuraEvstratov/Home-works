from itertools import *
matrix = "2 1356 245 35 2347 2 5".split()
graf = "БВ ЕВ ВА ВГ АГ ГК ГД АД".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break