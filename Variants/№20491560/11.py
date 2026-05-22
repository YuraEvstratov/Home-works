print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not((x or y) <= (z == x)):
                print(x, y, z)
# z-2 y-3 x-1