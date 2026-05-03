text = open("/Users/yura/Downloads/17-7.txt").readlines()
k = 0
summ = 0
for i in range(len(text) - 1):
    if (int(text[i]) % 3 == 0 or int(text[i + 1]) % 3 == 0) and ((int(text[i]) + int(text[i + 1])) % 5 == 0):
        k += 1
        summ = max(summ, int(text[i]) + int(text[i + 1]))
print(k, summ)