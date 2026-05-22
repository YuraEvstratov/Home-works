from itertools import *
word = "ПОЛИНА"
k = 0
for i in product(word, repeat=4):
    s = ''.join(i)
    if "ПЛ" not in s and "ЛП"not in s and "ПН"not in s and "НП"not in s and "НЛ" not in s and"ЛН" not in s and"ОИ" not in s and"ИО"not in s and "ОА"not in s and "АО"not in s and "ИА" not in s and"АИ":
        k += 1
print(k)
# неверно