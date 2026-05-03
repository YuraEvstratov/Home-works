from itertools import*

graf = "АБ БГ ГЕ ЕЗ ЗД ДВ АВ БВ ГД".split()
matrix = "67 567 456 35 234 123 12".split()

print("1 2 3 4 5 6 7")
for i in permutations("АБВГДЕЗ"):
    if all(str(i.index(m2) + 1) in matrix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break