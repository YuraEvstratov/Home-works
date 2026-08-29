text = open("/Users/yura/Downloads/24-3.txt").read()
left = 0
cnt_A = 0
cnt_B = 0
max_size = 0
for right in range(len(text)):
    if text[right]  == "A":
         cnt_A += 1
    if text[right]  == "B":
         cnt_B += 1
    while cnt_A > 1 or cnt_B > 1:  
        if text[left] == "A":
             cnt_A -=1
        if text[left] == "B":
             cnt_B -=1
        left += 1
    if cnt_A == 1 and cnt_B == 1:
         max_size = max(max_size, right - left + 1)
print(max_size)