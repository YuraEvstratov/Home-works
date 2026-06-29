from itertools import *

graf = "ЕА АБ БЖ ЖИ ИВ БД ДЖ ДВ ДИ АГ ЕГ ГБ ГЖ".split()
marix = "56 3478 247 23 168 1578 2368 2567".split()
print("1 2 3 4 5 6 7 8")
for i in permutations("АБВГДЕЖИ"):
    if all(str(i.index(m2) + 1) in marix[i.index(m1)] for m1, m2 in graf):
        print(*i)
        break