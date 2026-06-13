print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((x and y or (not(x))) and w or z):
                    print(w, x, y, z)
# z-1 x-2 y-3 w-4