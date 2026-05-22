print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = y and((not(w) or z) == x)
                print(w, x, y, z, int(F))
# w x y z F
# 0 1 1 0 1
# 1 0 1 0 1
# 1 0 1 1 0

#z-4 y-2 w-3 x-1