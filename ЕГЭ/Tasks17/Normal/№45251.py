text = open("/Users/yura/Downloads/107_17.txt")
s = [int(i) for i in text]
l = []
k = 0
for i in range(len(s)):
    if s[i] % 21 == 0:
        l.append(s[i])
med = min(l)
summ = 0
for i in range(len(s) - 1):
        if s[i] % med == 0 or s[i + 1] % med == 0:
            k += 1
            summ = max(summ, s[i] + s[i + 1])
print(k, summ)