text = open("/Users/yura/Downloads/zadanie24_1.txt").read()
k = 0
max_size = 0
for i in range(len(text)):
    if text[i] == "C":
        k += 1
    else:
        max_size = max(max_size, k)
        k = 0
max_size = max(max_size, k)
print(max_size)
