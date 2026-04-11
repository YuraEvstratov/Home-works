text = open("/Users/yura/Downloads/24-7.txt").readline()

max_len = 0
left = 0
values = {"A", "B", "C"}

for right in range(1, len(text)):
    if text[right] in values and text[right - 1] in values:
        left = right

    max_len = max(max_len, right - left + 1)

print(max_len)