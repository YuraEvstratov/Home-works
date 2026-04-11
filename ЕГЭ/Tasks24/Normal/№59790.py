text = open("/Users/yura/Downloads/24-6.txt").readline()

min_len = float("inf")
left = 0
count_T = 0

for right in range(len(text)):
    if text[right] == "T":
        count_T += 1
    while count_T == 210:
            min_len = min(min_len, right - left + 1)
            if text[left] == "T":
                count_T -= 1
            left += 1
        
print(min_len)