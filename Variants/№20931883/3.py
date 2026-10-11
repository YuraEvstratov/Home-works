text = open("/Users/yura/Downloads/24-5.txt").read()
max_s = 0
k = 0
i = 0
while i < len(text) - 2:
    if text[i] in "AO" and text[i + 1] in "AO" and text[i + 2] in "CDF":
        k += 1
        max_s = max(max_s, k)
        i += 3
    else:
        k = 0
        i += 1
print(max_s)
