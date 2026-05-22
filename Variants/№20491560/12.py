print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x and (not(y))) or (x == z) or (not(w))):
                    print(w, x, y, z)
# x-4 w-1 z-2 y-3