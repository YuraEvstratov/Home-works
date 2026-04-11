from itertools import *

matrix = "2468 18 578 16 368 145 38 12357".split()
graf = "АБ БВ ВЕ ЕК КИ ИЖ ЖГ ГА АИ ГИ БИ БЕ ЕИ".split()

print("1 2 3 4 5 6 7 8")
for i in permutations("АБВЕКИЖГ"):
    if all(str(i.index(c2) + 1) in matrix[i.index(c1)] for c1, c2 in graf):
        print(*i)
        break
# НЕ РАБОТАЕТ