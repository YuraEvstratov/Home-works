k = 0
for x in range(5):
    for y in range(5):
        for q in range(5):
            for z in range(5):
                for a in range(5):
                    k += 1
                    if x == 4 and y == 1 and q == 3 and z == 2 and a == 0:
                        print(k)