text = open("/Users/yura/Downloads/17-16.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if nums[j] % 10 == 7:
        l.append(nums[j])
x = min(l) ** 2
k = 0
max_summ = 0
for i in range(len(nums) - 1):
    if (str(nums[i])[-1] == str(nums[i + 1])[-1] and ((nums[i] % 7 == 0 and nums[i + 1] % 7 != 0) or (nums[i] % 7 != 0 and nums[i + 1] % 7 == 0)) and (nums[i] ** 2 + nums[i + 1]** 2) <= x):
        k += 1
        max_summ = max(max_summ, nums[i] ** 2 + nums[i + 1] ** 2)
print(k, max_summ)
