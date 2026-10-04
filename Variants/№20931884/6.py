print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (not(x) and z and not(y) and not(w)) or (not(x) and z and y and not(w)) or (not(x) and z and y and w):
                    print(w, x, y, z)
#z-4 x-1 y-2 w-3
