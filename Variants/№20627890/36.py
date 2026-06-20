from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:13]:
    for y in alph[:13]:
        n1 = int(f"8{x}78{y}", 13)
        n2 = int(f"79{x}{y}7", 18)
        if (n1 + n2) % 9 == 0:
            print((n1 + n2) // 9)
            break