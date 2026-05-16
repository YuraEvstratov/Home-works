file = open("/Users/yura/Downloads/17-5.txt")
text = [int(i) for i in file]
k = 0
max_raz = 0
for i in range(len(text) - 1):
    for j in range(i + 1, len(text)):
        if (text[i] - text[j]) % 60 == 0 and (text[i] % 15 == 0 or text[j] % 15 == 0):
            k += 1
            max_raz = max(max_raz, text[i] - text[j])
print(k, max_raz)