# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида:
# согласная  + гласная.
# Для выполнения этого задания следует написать программу.
text = open("/Users/yura/Downloads/24-2.txt").readline()
k = 0
m = 0
i = 0
while i < len(text):
    if (text[i]=='C' or text[i]=='D' or text[i]=='F') and (text[i+1]=='A' or text[i+1]=='O'):
        k += 1
        i += 2
    else:
        m = max(m, k)
        k = 0
        i += 1
m = max(m, k)
print(m)
