text = open("/Users/yura/Downloads/24_58328.txt").read()
k = 1
max_size = 1
for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        k += 1
    else:
        max_size = max(max_size, k)
        k = 1
max_size = max(max_size, k)
print(max_size)
