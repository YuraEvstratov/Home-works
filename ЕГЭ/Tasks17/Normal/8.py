text = open("/Users/yura/Downloads/17-3.txt").readlines()
max_summ = 0
len_values = 0
for i in range(len(text) - 1):
    for j in range(i + 1, len(text)):
        if (int(text[i]) + int(text[j])) % 7 == 0:
            len_values += 1
            max_summ = max(max_summ, int(text[i]) + int(text[j]))
print(len_values, max_summ)