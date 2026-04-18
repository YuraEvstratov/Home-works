text = open("/Users/yura/Downloads/24-2.txt").readline()
max_len = 0
for i in range(len(text)):
    for n in range(i + max_len, len(text)):
        c = text[i: n + 1]
        if all(c.count(x) < 101 for x in "UVWXYZ"):
            max_len = max(max_len, len(c))
        else :

            break
print(max_len)