text = open("/Users/yura/Downloads/24-2.txt").readline()

max_count = 0
for i in range(len(text)):
    for n in range(i + max_count, len(text)):
        c = text[i: n + 1]
        if c.count("A") == 1 and c.count("B") == 1:
            max_count = max(max_count, len(c))
        elif c.count("A") > 1 and c.count("B") > 1:
            break
print(max_count)