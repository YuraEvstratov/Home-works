from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:12]:
    for y in alph[:12]:
        n1 = int(f"{x}231{y}", 12)
        n2 = int(f"78{x}98{y}", 14)
        if (n1 + n2) % 99 == 0:
            print((n1 + n2) // 99)
            break