text = open("/Users/yura/Downloads/24_58329.txt").readline()
k = 1
m = 0
for i in range(len(text) - 2):
    if int(text[i]) + int(text[i + 1]) > int(text[i + 2]):
        k += 1
    else:
        k += 1
        m = max(k, m)
        k = 1
m = max(k, m)
print(m)