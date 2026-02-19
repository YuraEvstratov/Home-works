with open("/Users/yura/Desktop/Информатика/Fale_1.txt","r") as file:
    text = file.readlines()
    numbers = []
    value = ""
    rezult = 0
    idx = 0
    while not(len(text) == 1):
        idx = 0
        for i in range(0,len(text[0])):
            if text[0][idx].isdigit() == True:
                value += text[0][idx]
                idx += 1
            else:
                if value.isdigit() == True:
                    numbers.append(value)
                value = ""
                idx += 1
        if value.isdigit() == True:
            numbers.append(value)
            value = ""
        text.pop(0)
    idx = 0
    for i in range(0,len(text[0])):
            if text[0][idx].isdigit() == True:
                value += text[0][idx]
                idx += 1
            else:
                if value.isdigit() == True:
                    numbers.append(value)
                value = ""
                idx += 1
    if value.isdigit() == True:
            numbers.append(value)
    numbers = list(map(int,numbers))
    print(numbers)
    print(sum(numbers)/len(numbers))
    