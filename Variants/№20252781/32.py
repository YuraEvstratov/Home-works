from itertools import *
word = "СТРОКА"
count = 0
l = []
for s in product(sorted(word), repeat = 5):
    count += 1
    if count % 2 == 0 and s.count("О") == 2 and s[0] not in ('АСТ'):
        l.append(count)
print(max(l))