text = open("/Users/yura/Downloads/24-2.txt").read()
left = 1
cnt_W = 0
max_size = 0
for right in range(len(text) - 2):
    if text[right]  == "W" and text[right + 1] == "W":
        cnt_W += 1
    while cnt_W == 100:
        max_size = max(max_size, right - left + 1)
        if text[left] == "W" and text[left + 1] == "W":
            cnt_W -=1
        left += 2
print(max_size)