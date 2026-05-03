print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((z == (x <= w)) and (x == (not(w <= y)))):
                    print(w, x, y, z)
#y-1 w-4 x-3 z-2