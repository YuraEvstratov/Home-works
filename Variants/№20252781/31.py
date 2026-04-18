words = {"Е": 0, "Ж": 1, "И": 2}
k = 0
for x in range(3):
    for y in range(3):
        for z in range(3):
            for q in range(3):
                for w in range(3):
                    k += 1
                    if k == 238:
                        print(x, y, z, q, w)
# И И И Ж Е