text = open("/Users/yura/Downloads/demo_2025_17.txt").readlines()
k = 0
summ = 0
l = []
for i in range(len(text)):
    l.append(int(text[i]))
g = min(l)
for i in range(len(text) - 1):
    if int(text[i]) % 16 == g or int(text[i + 1]) % 16 == g:
        k += 1
        summ = max(summ, int(text[i]) + int(text[i + 1]))
print(k, summ)