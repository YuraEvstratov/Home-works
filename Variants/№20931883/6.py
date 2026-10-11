text = open("/Users/yura/Downloads/24-6.txt").read()
k = 0
left = 0
max_k = float("inf")
count_T = 0
for right in range(len(text)):
    if text[right] == "T":
        count_T += 1
    while count_T > 100:
        if text[left] == "T":
            count_T -= 1
        left += 1
    if count_T == 100:
        max_k = min(max_k, right - left + 1 - 2)
print(max_k)
