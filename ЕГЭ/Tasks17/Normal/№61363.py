text = open("/Users/yura/Downloads/17_2024.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if abs(nums[j]) % 100 == 19:
        l.append(nums[j])
s = max(l)
k = 0
max_sm = 0
for i in range(len(nums) - 2):
    if ((999 < nums[i] < 10000 and 999 < nums[i + 1] < 10000 and not(999 < nums[i + 2] < 10000)) or (not(999 < nums[i] < 10000) and 999 < nums[i + 1] < 10000 and 999 < nums[i + 2] < 10000) or (999 < nums[i] < 10000 and not(999 < nums[i + 1] < 10000) and 999 < nums[i + 2] < 10000)) and ((nums[i] + nums[i + 1] + nums[i + 2]) > s) and (nums[i] % 3 == 0 and nums[i + 1] % 3 == 0 and nums[i + 2] % 3 == 0) :
        k += 1
        max_sm = max(max_sm, nums[i]  + nums[i + 1] + nums[i + 2])
print(k, max_sm)
