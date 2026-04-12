text = open("/Users/yura/Downloads/24_59848.txt").readline()
words = "0123456789ABCDEFJHIGKLNM"
max_len = 0
x = 0

for i in range(len(text)):
    if text[i] in words:
        if text[0] != "0":
            x += 1
        max_len = max(max_len, x)
    else:
        x = 0
max_len = max(max_len, x)
print(max_len)