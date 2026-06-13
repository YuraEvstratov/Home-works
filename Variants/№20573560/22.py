k = 0
word = "ЕИОРТЯ"
for i in word:
    for r in word:
        for q in word:
            for t in word:
                for a in word:
                    for f in word:
                        d = i + r + q + t + a + f
                        k += 1
                        if k % 2 != 0 and (d[0] != "И" or d[0] != "Е" or d[0] != "О") and d.count("Т") == 1:
                            print(k)                       