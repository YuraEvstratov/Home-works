arr = {0:"А", 1:"К", 2:"Р", 3:"У"}
k = 0
size = len(arr)
for i in range(0,size):
    for y in range(0,size):
        for g in range(0,size):
            for z in range(0,size):
                for e in range(0,size):
                    k += 1
                    if i == 3 and y == 1 and g == 0 and z == 2 and e == 0:
                        print(k)
                        break