from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:10]:
    n1 = int(f'4C{x}4', 15)
    n2 = int(f'{x}62A', 13)
    res = n1 + n2
    if res % 121 == 0:
        print(res // 121)
        break