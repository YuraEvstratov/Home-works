from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:17][::-1]:
    n1 = int(f'8{x}5678', 25)
    n2 = int(f'457{x}69', 25)
    n3 = int(f'145{x}1', 25)
    res = n1 + n2 + n3
    if res % 23 == 0:
        print(res // 23)
        break