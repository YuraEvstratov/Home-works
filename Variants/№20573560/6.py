print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if not((not(a) and not(b)) or (b == c) or d):
                    print(a, b, c, d)
# d-2 c-1 a-4 b-3