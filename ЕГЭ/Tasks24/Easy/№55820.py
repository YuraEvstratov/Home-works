text = open("/Users/yura/Downloads/24-10.txt").read()
max_cnt = 0
k = 1
symbols = "QRS"
for i in range(len(text) - 1):
    if text[i] not in symbols or text[i + 1] not in symbols:
        k += 1
        max_cnt = max(max_cnt, k)
    else:
        k = 1
print(max_cnt)