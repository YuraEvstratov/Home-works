from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:13]:
    n1 = int(f"8{x}71", 13)
    n2 = int(f"3{x}DF", 17)
    if (n1 + n2) % 197 == 0:
        print((n1 + n2) // 197)