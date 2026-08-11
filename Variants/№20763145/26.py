k = 0
for x in range(8):
    for y in range(8):
        for z in range(8):
            for q in range(8):
                k += 1
                if x == 1 and y == 5:
                    print(k)
                    break