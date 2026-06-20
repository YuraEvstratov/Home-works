text = open("/Users/yura/Downloads/24-11.txt").read().split("A")
k = 0
for i in range(len(text)):
    if text[i].count("B") == 0 and len(text[i]) >= 8:
        k += 1
print(k)