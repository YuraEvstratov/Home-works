text = open("/Users/yura/Downloads/24-4.txt").readline()
vowels = "AEIOUY"
k = 0
count_vowels = 0
count_z = 0
left = 0
min_size = float("inf")
for i in range(len(text)):
    if text[i] == "Z":
        count_z += 1
    if text[i] in vowels:
        count_vowels += 1
    while count_z > 72 or count_vowels > 1:
        if text[left] == "Z":
            count_z -= 1
        if text[left] in vowels:
            count_vowels -= 1
        left += 1
    if count_z == 72 and count_vowels == 1 and text[i] in vowels:
        k = i - left + 1
        min_size = min(min_size, k)
print(min_size)
        
