file = open("/Users/yura/Downloads/17-7.txt")
text = [int(i) for i in file]
k = 0
max_sum = 0
for i in range(len(text) - 2):
    if (text[i] < (text[i + 1] + text[i + 2])) and (text[i + 1] < (text[i] + text[i + 2])) and (text[i + 2] < (text[i + 1] + text[i])):
        k += 1
        max_sum = max(max_sum, text[i] + text[i + 1] + text[i + 2])
print(k, max_sum)