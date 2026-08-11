print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((w <= x) or (y <= z)) and ((x == y) <= (w == z))):
                    print(x, y, z, w)
#w-3 z-2 y-4 x-1
