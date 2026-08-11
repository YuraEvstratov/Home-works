from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:9]:
    for y in alph[:9]:
        n1 = int(f'2{y}66{x}', 9)
        n2 = int(f'{x}0{y}1', 12)
        res = n1 + n2
        if res % 170 == 0:
            print(res // 170)
            break
        