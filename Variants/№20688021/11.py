print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x <= (not(y == w))) and (y or (w <= z))):
                    print(w, x, y, z)
#x-4 w-1 y-3 z-2