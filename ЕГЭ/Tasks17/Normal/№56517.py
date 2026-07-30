text = open("/Users/yura/Downloads/17-16.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if abs(nums[j]) % 10 == 3:
        l.append(nums[j])
x = min(l) ** 2
k = 0
max_sum = 0
nums = [abs(i) for i in nums]
for i in range(len(nums) - 1):
    if (nums[i] % 10 == nums[i + 1] % 10) and ((nums[i] % 3 == 0 and nums[i + 1] % 3 != 0) or (nums[i] % 3 != 0 and nums[i + 1] % 3 == 0)) and (nums[i] ** 2 + nums[i + 1] ** 2) <= x:
        k += 1
        max_sum = max(max_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(k, max_sum)
    