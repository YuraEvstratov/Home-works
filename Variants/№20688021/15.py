print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x and not(y)) or (x == z) or w):
                    print(w, x, y, z)
#w-3 y-1 z-4 x-2