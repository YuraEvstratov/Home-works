text = open("/Users/yura/Downloads/24-9.txt").readline().split("F")
m = 0
k = 1
for i in range(len(text)):
    if text[i].count('A') <= 2:
        k += len(text[i]) + 1
        m = max(m, k)
    else:
        k = 1
print(m)