from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
for x in alph[:22][::-1]:
    n1 = int(f"63{x}89875", 22)
    n2 = int(f"17{x}51", 22)
    n3 = int(f"75{x}3", 22)
    res = n1 + n2 + n3
    if res % 21 == 0:
        print(res // 21)
        