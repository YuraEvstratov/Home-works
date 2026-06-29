text = open("/Users/yura/Downloads/demo_2025_24.txt").read()
max_cnt = 0
k = 1
opns = "-*"
nums = "6789"
for i in range(len(text) - 1):
    if k == 0 and text[i] == "0" and text[i + 1] in nums:
        max_cnt = max(max_cnt, k)
        k = 0
    if ((text[i] in opns and text[i + 1] in opns)):
        max_cnt = max(max_cnt, k)
        k = 0
    k += 1
print(max_cnt)