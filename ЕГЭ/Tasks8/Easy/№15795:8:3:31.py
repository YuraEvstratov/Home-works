arr = {0:"А", 1:"П", 2:"Р", 3:"С", 4:"У"}
k = 0
size = len(arr)
for i in range(0,size):
    for y in range(0,size):
        for g in range(0,size):
            for j in range(0,size):
                k += 1
                if i != 0 and y != 0 and g != 0 and j != 0:
                    print(k)