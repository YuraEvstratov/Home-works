from itertools import*

graf = "АВ ВД ВГ ГБ ГЕ ЕК".split()
matrix = "3 3 124 356 4 47 6".split()

print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕК"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break