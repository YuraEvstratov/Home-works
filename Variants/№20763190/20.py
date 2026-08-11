from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:8]:
    for y in alph[:8]:
        n1 = int(f"{y}04{x}5", 11)
        n2 = int(f"253{x}{y}", 8)
        res = n1 + n2
        if res % 117 == 0:
            print(res // 117)
            
        