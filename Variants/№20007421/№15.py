arr = {0:"А", 1:"М", 2:"Р", 3:"Т"}
k = 0
size = len(arr)
for i in range(0,size):
    for y in range(0,size):
        for q in range(0,size):
            for j in range(0,size):
                k += 1
                if k == 250:
                    print(arr[i],arr[y],arr[q],arr[j])