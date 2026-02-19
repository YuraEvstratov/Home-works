with open("/Users/yura/Desktop/Информатика/Fale_1.txt","r") as file:
    text = file.read()
    values = {}
    for i in range(0,len(text)):
        if text[i] != "\n":
            values[text[i]] = values.get(text[i], 0) + 1
max_value = max(dict.values(values))
rezult = ""
for key, nums in values.items():
    if nums == max_value:
        rezult = key
        break
print(rezult)