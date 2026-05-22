from itertools import*
word = "0n2n4n6n8nAnCDEn"
k = 0
for i in product(word, repeat=4):
    i = ''.join(i)
    if i[0] != "0" and i.count("D") == 1:
        if "Dn" not in i and "nD" not in i:
            k += 1
print(k)    