print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x and not(y)) or (x == z) or w):
                    print(w, x, y, z)
# y-1  x-2  w-3  z-4