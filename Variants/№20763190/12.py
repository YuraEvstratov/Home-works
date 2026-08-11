from string import digits , ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:11]:
    n1 = int(f'95{x}2', 11)
    n2 = int(f'{x}458', 12)
    res = n1 + n2
    if res % 136 == 0:
        print(res // 136)
        break