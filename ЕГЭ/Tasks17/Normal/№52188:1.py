text = open("")
nums = [int(i) for i in text]
l = []
for j in range(len(text)):
    if abs(text[j]) % 10 == 3:
        l.append(text[j])
x = min(l) ** 2
k = 0
max_sum = 0
for i in range(len(nums) - 1):
    if min(text[i], text[i + 1]) % 10 == 3 and (text[i] ** 2 + text[i + 1] ** 2) < x:
        k += 1
        max_sum = max(max_sum, text[i] ** 2 + text[i + 1] ** 2)
print(k, max_sum)
