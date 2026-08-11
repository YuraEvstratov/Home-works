print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x and not(y)) == (z <= w)):
                    print(x, y, z, w)
print("")
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not(x) == y) and (z <= w)):
                    print(x, y, z, w)
# z-1 x-2 y-3 w-4
