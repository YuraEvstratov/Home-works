arr = {0:"Е", 1:"Н", 2:"О", 3:"С"}
k = 0
size = len(arr)
for i in range(0, size):
    for y in range(0, size):
        for x in range(0, size):
            for z in range(0, size):
                k += 1
                if i == 3:
                    print(k)
                    break