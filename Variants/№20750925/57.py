text = open("/Users/yura/Downloads/24-9.txt").read()
max_size = 0
value = 0
glasn = "AO"
sogl = "CDF"
i = 0
while i < len(text) - 2:
    if text[i] in glasn and text[i + 1] in glasn and text[i + 2] in sogl:
        value += 1
        i += 3
        max_size = max(max_size, value)
    else:
        i += 1    
        value = 0
print(max_size)
