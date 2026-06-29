from itertools import *
word = "ЯРОСЛАВ"
k = 0
for i in permutations(word, 5):
    i = ''.join(i)
    if ((i.count("Р") + i.count("С") + i.count("Л") + i.count("В")) > (i.count("Я") + i.count("О") + i.count("А")) and
        i.count("ЯО") == 0 and i.count("ОЯ") == 0 and i.count("ЯА") == 0 and i.count("АЯ") == 0 and i.count("АО") == 0 and i.count("ОА") == 0 ):
        k += 1 
print(k)
