word = "ВЛТУ"
k = 0
for q in word:
    for r in word:
        for f in word:
            for a in word:
                k += 1
                if k == 98:
                    print(q, r, f ,a)