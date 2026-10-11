print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (x == (not(w == y))) and (w == (y <= z)):
                    print(w, x, y, z)
#w-4 z-2 y-1 x-3
