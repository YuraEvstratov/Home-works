text = open("/Users/yura/Downloads/17-9.txt")
s = [int(i) for i in text]
l = []
k = 0
for i in range(len(s)):
    if s[i] % 2 == 0:
        l.append(s[i])
med = sum(l) / len(l)
summ = 0
for i in range(len(s) - 1):
        if (s[i] % 3 == 0 or s[i + 1] % 3 == 0) and (s[i] < med or s[i + 1] < med):
            k += 1
            summ = max(summ, s[i] + s[i + 1])
print(k, summ)