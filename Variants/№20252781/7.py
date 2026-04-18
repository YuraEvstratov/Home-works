print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((w == x) and (y <= z)):
                    print(w, x, y, z)
print("")
print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((w == x) and (y <= z)):
                    print(w, x, y, z)


print("")
print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((w <= x) <= (y == z)):
                    print(w, x, y, z)


#y-2 z-1 w-3 x-4