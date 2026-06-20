text = open("/Users/yura/Downloads/24-9.txt").readline()
k = 0
i = 0
sogl = "CDF"
glasn = "AO"
max_cnt = 0
while i != len(text) - 2:
    if ((text[i] in sogl) and
        (text[i + 1] in sogl) and
        (text[i + 2] in glasn)):
        k += 1
        i += 3
    else:
        max_cnt = max(max_cnt, k)
        k = 0
        i += 1
max_cnt = max(max_cnt, k)
print(max_cnt)
    