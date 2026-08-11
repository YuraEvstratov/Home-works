from itertools import product
k = 0
s = product("АБРТЫ", repeat= 5)
for i in s:
    x = "".join(i)
    k += 1
    if x.count("Ы") == 0 and x.count("АА") == 0:
        print(k)
        break
        