text = open("/Users/yura/Downloads/zadanie24_2.txt").read()
k = 0
max_k = 0
for i in range(len(text) - 2):
    if text[i] == "L" and text[i + 1] == "D" and text[i + 2] == "R":
        k += 1
        i += 2
    else:
        max_k = max(k, max_k)
print(max_k)
