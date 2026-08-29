k = 0
for x in range(4):
    for y in range(4):
        for q in range(4):
            for z in range(4):
                k += 1
                if k == 215:
                    print(x, y, q, z)
                    