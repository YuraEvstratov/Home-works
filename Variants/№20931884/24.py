k = 0
for i in range(4):
    for x in range(4):
        for z in range(4):
            for q in range(4):
                k += 1
                if k == 249:
                    print(i, x, z, q)
                    