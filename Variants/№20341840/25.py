words = "0-А 1-К 2-Р 3-У"
k = 0
for x in range(4):
    for y in range(4):
        for z in range(4):
            for q in range(4):
                for l in range(4):
                    k += 1
                    if k == 350:
                        print(x,y,z,q,l)
#КККУК
