text = open("/Users/yura/Downloads/24-9.txt").readline()
k = 0
chek = 0
i = 0
while i < len(text):
    if (text[i] == "C" or 
        text[i] == "D" or
        text[i] == "F") and (text[i + 1] == "A" or
                             text[i + 1] == "O"):
        k += 1
        i += 2
    else:
        chek = max(chek, k)
        i += 1
        k = 0
chek = max(chek, k)
print(chek)