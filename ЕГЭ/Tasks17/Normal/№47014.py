text = open("/Users/yura/Downloads/17-10.txt")
s = [int(i) for i in text]
l = []
k = 0
for i in range(len(s)):
    if s[i] % 2 != 0:
        l.append(s[i])
med = sum(l) // len(l)
summ = 0
for i in range(len(s) - 1):
        if (s[i] % 5 == 0 and s[i + 1] < med) or (s[i] < med and s[i + 1] % 5 == 0):
            k += 1
            summ = max(summ, s[i] + s[i + 1])
print(k, summ)