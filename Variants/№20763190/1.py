from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:31][::-1]:
    n1 = int(f'123{x}AB3', 31)
    n2 = int(f'3CE{x}321', 31)
    res = n1 + n2
    if res % 17 == 0:
        print(res // 17)
        break