from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:22]:
    n1 = int(f"98{x}79641", 22)
    n2 = int(f"25{x}49", 22)
    n3 = int(f"63{x}5", 22)
    res = n1 + n2 + n3
    if res % 21 == 0:
        print(res // 21)
        