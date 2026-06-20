from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:15]:
    for y in alph[:15]:
        n1 = int(f"90{x}4{y}", 15)
        n2 = int(f"91{x}{y}2", 16)
        if (n1 + n2) % 56 == 0:
            print((n1 + n2) // 56)
            break