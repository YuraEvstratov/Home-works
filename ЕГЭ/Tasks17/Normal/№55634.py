text = open("/Users/yura/Downloads/17-17.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if str(nums[j])[-1] == str(nums[j])[-2]:
        l.append(nums[j])
x = min(l) ** 2
k = 0
max_sum = 0
for i in range(len(nums) - 1):
    if ((str(nums[i])[-1] == str(nums[i + 1])[-2]) or (str(nums[i + 1])[-1] == str(nums[i])[-2])) and ((nums[i] % 13 == 0 and nums[i + 1] % 13 != 0) or (nums[i + 1] % 13 == 0 and nums[i] % 13 != 0)) and (nums[i] ** 2 + nums[i + 1] ** 2) <= x:
        k += 1
        max_sum = max(max_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(k, max_sum)
    