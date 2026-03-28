print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(not(x <= w) or ( y == z) or y):
                    print(w, x, y, z)
#z-1 y-4 x-2 w-3