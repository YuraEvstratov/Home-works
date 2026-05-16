file = open("/Users/yura/Downloads/17-7.txt")
text = [int(i) for i in file]
k = 0
max_sum = 0
for i in range(len(text) - 1):
    if (text[i] + text[i + 1]) % 7 == 0 and (text[i] * text[i + 1]) % 15 == 0:
        k += 1
        max_sum = max(max_sum, text[i] + text[i + 1])
print(k, max_sum)