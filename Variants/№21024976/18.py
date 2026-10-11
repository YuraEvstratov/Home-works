k = 0
for x in range(4):
    for y in range(4):
        for z in range(4):
            for s in range(4):
                for a in range(4):
                    k += 1
                    if k == 250:
                        print(x, y, z, s, a)