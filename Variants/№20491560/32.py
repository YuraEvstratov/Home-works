wo = {0:"В", 1:"Н", 2:"Р", 3:"Т"}
k = 0
for x in range(4):
    for w in range(4):
        for s in range(4):
            for z in range(4):
                k += 1
                if k == 250:
                    print(wo[x], wo[w], wo[s], wo[z])