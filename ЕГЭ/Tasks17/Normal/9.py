text = open("/Users/yura/Downloads/17-4.txt").readlines()
len_values = 0
max_summ = 0
for i in range(len(text) - 1):
    for j in range(i + 1, len(text)):
        if (int(text[i]) + int(text[j])) % 80 == 0 and (int(text[i]) % 50 == 0 or int(text[j]) % 50 == 0):
            len_values += 1
            max_summ = max(max_summ, int(text[i]) + int(text[j]))
print(len_values, max_summ)