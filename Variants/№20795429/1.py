text = open("/Users/yura/Downloads/24-4.txt").read()
max_size = 0
value = 0
l = "0123456789"
nums = []
for i in range(len(text)):
    if len(nums) == 10:
        max_size = max(max_size, value)
    value += 1
    if text[i] not in l:
        nums = []
        value = 0
    if text[i] in l and text[i] not in nums:
        nums.append(text[i])
print(max_size)
