text = open("/Users/yura/Downloads/1777.txt").readline()
text = [int(i) for i in text]
k = 0
max_summ = 0
l = []
for j in range(len(text)):
    if int(text[j]) % 100 == 29:
        l.append(int(text[j]))
max_num = max(l)
for i in range(len(text) - 2):
    if ((10000 <= int(text[i]) <= 99999 and 10000 <= int(text[i + 1]) <= 99999 and not(10000 <= int(text[i + 2]) <= 99999)) or (10000 <= int(text[i]) <= 99999 and 10000 <= int(text[i + 2]) <= 99999 and not(10000 <= int(text[i + 1]) <= 99999)) or (10000 <= int(text[i + 2]) <= 99999 and 10000 <= int(text[i + 1]) <= 99999 and not(10000 <= int(text[i]) <= 99999))) and ((int(text[i]) + int(text[i + 1]) + int(text[i + 2])) > max_num):
        k += 1
        max_summ = max(max_summ, (int(text[i]) + int(text[i + 1]) + int(text[i + 2])))