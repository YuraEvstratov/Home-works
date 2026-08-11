from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:37]:
    n1 = int(f'32{x}437', 37)
    n2 = int(f'5{x}2937', 37)
    res = n1 + n2
    if res % 63 == 0:
        print(res // 63)
        break