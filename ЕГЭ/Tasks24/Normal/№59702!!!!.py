text = open("/Users/yura/Downloads/24-2.txt").read()
left = 0
count_Y = 0
max_size = 0
for right in range(len(text)):
    if text[right] == "Y":
        count_Y += 1
    while count_Y == 150:
        max_size = max(max_size, right - left + 1)
        if text[left] == "Y":
            count_Y -= 1
        left += 1
print(max_size)