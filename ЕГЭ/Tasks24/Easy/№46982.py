text = open("/Users/yura/Downloads/24-11.txt").readline().split("E")
k = 0
for i in text:
    if len(i) >= 10 and i.count("F") == 0:
        k += 1
print(k)