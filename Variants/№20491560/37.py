from itertools import*
k = 0
for i in product(sorted("ХШЮЕЖЧЭВ"), repeat= 4):
    k += 1
    s = ''.join(i)
    if s[0] != "В" and s[-1] != "В" and s.count("Ч") >= 3 and k % 2 != 0:
        print(k)
        break
