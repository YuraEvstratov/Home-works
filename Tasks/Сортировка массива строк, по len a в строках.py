with open("/Users/yura/Desktop/Информатика/Fale_1.txt",'r') as file:
    text = file.readlines()
    print(text)
    for i in range(1, len(text)):
        key = text[i]
        j = i - 1
        while j >= 0 and text[j].count("a") > key.count("a"):
            text[j + 1] = text[j]
            j -= 1
        text[j + 1] = key
    print(text)