print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not(not(x) or ((w <= y) <= z)):
                    print(w, x, y, z)
# x-2 z-4 y-3 w-1