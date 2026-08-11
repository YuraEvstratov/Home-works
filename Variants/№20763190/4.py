from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:9]:
    for y in alph[:9]:
        n1 = int(f'88{x}4{y}', 9)
        n2 = int(f'7{x}44{y}', 11)
        res = n1 + n2
        if res % 61 == 0:
            print(res // 61)
            break