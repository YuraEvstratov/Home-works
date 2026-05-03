print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x and y) or (y == z) or w):
                    print(w, x, y, z)
#w-1 z-2 y-3 x-4