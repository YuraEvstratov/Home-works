text = open("/Users/yura/Downloads/24-4.txt").readline()
count_Z = 0 
mixn_size = float("inf")
left = 0
count_Glasn = 0
glasn = "AEIOUY"
for right in range(len(text)):
    if text[right] == "Z":
        print(count_Z)
    if text[right] in glasn:
        count_Glasn += 1
    while count_Z == 72 and count_Glasn == 1:
        mixn_size = min(mixn_size, right - left + 1)
        if text[left] == "Z":
            count_Z -= 1
        if text[left] in glasn:
            count_Glasn -= 1
        left += 1

print(mixn_size)
