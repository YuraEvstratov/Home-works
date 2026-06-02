nums = open("/Users/yura/Downloads/17-3.txt")
text = [int(i) for i in nums]
k = 0
max_summ = 0
for i in range(len(text) - 1):
    for j in range(i + 1, len(text)):
        if ((int(text[i]) - int(text[j])) % 2 == 0 )and ((int(text[i])) % 19 == 0 or (int(text[j])) % 19 == 0):
            k += 1
            max_summ = max(max_summ, int(text[i]) + int(text[j]))
print(k, max_summ)