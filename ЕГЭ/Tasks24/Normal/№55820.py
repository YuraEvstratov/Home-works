text = open('/Users/yura/Downloads/24-10.txt').readline()
k = 0
m = 0
for i in range(len(text) - 1):
    if text[i] not in "QRS" or text[i + 1] not in "QRS":
        k += 1
        m = max(k, m)
    else:
        k = 1
print(m)