words = {"A": 0, "Г": 1, "И": 2, "Л": 3, "М": 4, "О": 5, "Р": 6, "Т": 7}
k = 0
for x in range(8):
    for y in range(8):
        for z in range(8):
            for w in range(8):
                k += 1
                if x == 1 and y == 5:
                    print(k)
                    break