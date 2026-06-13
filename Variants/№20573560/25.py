from itertools import *
word = "СКАНЕР"
k = 0
cnt = 0
for i in product(sorted(word), repeat= 10):
    k += 1
    if k % 3 == 0 and i[0] != "А" and i[0] != "Е"  and i.count("Р") == 1:
        cnt += 1
print(cnt)