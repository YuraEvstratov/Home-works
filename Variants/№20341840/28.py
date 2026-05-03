words = "0-K 1-O 2-P"
k = 0
for i in range(3):
    for x in range(3):
        for y in range(3):
            for z in range(3):
                for q in range(3):
                    k += 1
                    if k == 238:
                        print(i, x, y, z, q)
#PPPOK