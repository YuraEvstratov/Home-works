text = open("/Users/yura/Downloads/24-5.txt").read()
words = set("QWERTYUIOPASDFGHJKLZXCVBNM")
found = set()
k = 0
max_size = 0
for i in text:
    if i in words:
        found.add(i)
        k += 1
        if words == found:
            max_size = max(max_size, k)
    else:
        found.clear()
        k = 0
print(max_size)
            

