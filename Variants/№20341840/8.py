print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x <= (z <= w)) and (z <= (y == (not(w))))):
                    print(w, x, y, z)
#w-3 y-4 x-2 z-1