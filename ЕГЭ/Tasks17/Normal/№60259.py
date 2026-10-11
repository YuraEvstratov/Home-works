text = open("/Users/yura/Downloads/17_2024.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if abs(nums[j]) % 100 == 13:
        l.append(nums[j])
s = max(l)
k = 0
max_sm = 0
for i in range(len(nums) - 2):
    if ((99 < nums[i] < 1000 and 99 < nums[i + 1] < 1000 and not(99 < nums[i + 2] < 1000)) or (not(99 < nums[i] < 1000) and 99 < nums[i + 1] < 1000 and 99 < nums[i + 2] < 1000) or (99 < nums[i] < 1000 and not(99 < nums[i + 1] < 1000) and 99 < nums[i + 2] < 1000)) and (nums[i] + nums[i + 1] + nums[i + 2]) < s:
        k += 1
        max_sm = max(max_sm, nums[i]  + nums[i + 1] + nums[i + 2])
print(k, max_sm)
