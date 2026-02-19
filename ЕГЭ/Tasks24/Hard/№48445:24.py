# Текстовый файл содержит только буквы A, C, D, F, O. Определите максимальное количество идущих подряд групп символов вида:
# согласная + согласная + гласная.
text = open("/Users/yura/Downloads/24-2.txt").readline()
k = 0
m = 0
i = 0
while i < len(text):
    if (text[i] == "C" or text[i] == "D" or text[i] == "F") and (text[i + 1] == "C" or text[i + 1] == "D" or text[i + 1] == "F") and (text[i + 2] == "A" or text[i + 2] == "O"):
        k += 1
        i += 3
    else:
        m = max(m, k)
        k = 0
        i += 1
m = max(m, k)
print(m)