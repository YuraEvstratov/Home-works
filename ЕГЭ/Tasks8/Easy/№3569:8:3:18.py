arr = {0:"А", 1:"М", 2:"У", 3:"Х"}
k = 0
size = len(arr)
for i in range(0,size):
    for y in range(0,size):
        for g in range(0,size):
            for j in range(0,size):
                k += 1
                if k == 254:
                    print(arr[i],arr[y],arr[g],arr[j])
                    break