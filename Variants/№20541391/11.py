k  = 0 
for x in range(4):
    for y in range(4):
        for u in range(4):
            for q in range(4):
                k += 1
                if x == 3 and y == 2 and u == 1 and q == 0:
                    print(k)
                    break