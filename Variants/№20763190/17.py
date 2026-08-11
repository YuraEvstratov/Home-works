from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:12][::-1]:
    n1 = int(f"2AB{x}", 12)
    n2 = int(f"{x}8E", 17)
    res = n1 + n2 
    if res % 27 == 0:
        print(res // 27)
        