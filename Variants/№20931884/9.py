print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (x == (not(y))) <= ((z <= (not(w))) and (w <=(not(y)))):
                    print(w, x, y, z)
#y-4 z-3 x-1 w-2
