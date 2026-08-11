from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:12]:
    for y in alph[:12]:
        n1 = int(f'{y}AA{x}', 12)
        n2 = int(f'{x}02{y}', 14)
        res = n1 + n2 
        if res % 80 == 0:
            print(res // 80)
            break