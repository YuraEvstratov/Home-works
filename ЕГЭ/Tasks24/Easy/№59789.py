text = open("/Users/yura/Downloads/24-6.txt").readline()

max_len = 0
left = 0
count_Y = 0

for right in range(len(text)):
    if text[right] == "Y":
        count_Y += 1
    while count_Y > 100:
        if text[left] == "Y":
            count_Y -= 1
        left += 1
    max_len = max(max_len, right - left + 1)

print(max_len)

# ABCYAC.....Y