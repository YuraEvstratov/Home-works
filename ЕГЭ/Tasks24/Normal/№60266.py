text = open("/Users/yura/Downloads/24_2024.txt").read()
left = 0
cnt_T = 0
max_size = 0
for right in range(len(text) - 2):
    if text[right]  == "T":
        cnt_T += 1
    while cnt_T == 100:
        max_size = max(max_size, right - left + 1)
        if text[left] == "T":
            cnt_T -=1
        left += 1
print(max_size)