from itertools import *

graf = "АГ ГД АД ДЕ ЕБ ЕК БК БВ".split()
marix = "27 17 56 6 367 345 125".split()
print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break