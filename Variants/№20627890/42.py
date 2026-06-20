from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:12]:
    n1 = int(f"3{x}DA", 14)
    n2 = int(f"5{x}A6", 12)
    if (n1 + n2) % 81 == 0:
        print((n1 + n2) // 81)
