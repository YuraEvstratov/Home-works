print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((x <= (not(y))) and (x or w)) <= (not(z))):
                    print(x, y, z, w)
#z-3 y-2 w-1 x-4
