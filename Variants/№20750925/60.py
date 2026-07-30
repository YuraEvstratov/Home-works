text = open("/Users/yura/Downloads/24-6.txt").read()
left = 0
min_size = float("inf")
count_V = 0
for right in range(len(text)):
    if text[right] == "V":
        count_V += 1
    while count_V == 120:
        min_size = min(min_size, right - left + 1)
        if text[left] == "V":
            count_V -= 1
        left += 1
print(min_size)