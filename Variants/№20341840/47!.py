text = open("/Users/yura/Downloads/17-8.txt").readlines()
k = 0
summ = 0
l = []
for w in range(len(text)):
    l.append(int(text[w]))
g = min(l) ** 2
for i in range(len(text) - 1):
    if (text[i] == "7" and text[i + 1] != "7") or (text[i + 1] == "7" and text[i] != "7") and (int(text[i]) ** 2 + int(text[i + 1]) ** 2) < g:
        k += 1
        summ = max(summ, int(text[i]) + int(text[i + 1]))
print(k, summ)