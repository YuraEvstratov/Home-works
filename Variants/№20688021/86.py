text = open("/Users/yura/Downloads/24-7.txt").read()
max_cnt = 0
k = 0
word = "ABC"
for i in range(len(text) - 1):
    k += 1
    if text[i] in word and text[i + 1] in word:
        max_cnt = max(max_cnt, k)
        k = 0
max_cnt = max(max_cnt, k)
print(max_cnt)