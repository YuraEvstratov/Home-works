print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((not(x) == z) <= (y == (w or x))):
                    print(w, x, y, z)
# y-1 z-4 x-2 w-3