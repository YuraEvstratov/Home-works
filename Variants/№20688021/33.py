k = 0
for x in range(3):
    for y in range(3):
        for z in range(3):
            for q in range(3):
                for t in range(3):
                    k += 1
                    if k == 240:
                        print(x, y, z, q, t)