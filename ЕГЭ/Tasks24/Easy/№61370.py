text = open("/Users/yura/Downloads/24-3.txt").read()
c_A = 0
c_B = 0
left = 0
max_size = 0
for right in range(len(text) - 1):
    if text[right] == "A":
        c_A += 1
    elif text[right] == "B":
        c_B += 1
    while c_B > 1 or c_A > 1:
        if text[left] == "A":
            c_A -= 1
        elif text[left] == "B":
                c_B -= 1
        left += 1
    if c_A == 1 and c_B == 1:
         max_size = max(max_size, right - left + 1)
print(max_size)
