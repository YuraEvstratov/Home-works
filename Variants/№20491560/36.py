from itertools import*
k = 0
for i in product("АЕЛПРЬ", repeat= 6):
    k += 1
    s = ''.join(i)
    if k % 2 !=0 and s[0] != "А" and s[0] != "Л" and s.count("П") >= 2:
        print(k)
        break