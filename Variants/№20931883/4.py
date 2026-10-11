text = open("/Users/yura/Downloads/24_demo.txt").read()
k = 1
max_s = 0
for i in range(len(text) - 1):
    if text[i] == "Y" and text[i + 1] == "Y":
        k += 1
        m = max(max_s, k)
    else:
        k = 1
print(max_s)
