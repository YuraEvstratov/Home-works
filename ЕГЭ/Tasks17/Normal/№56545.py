text = open("/Users/yura/Downloads/17.txt")
nums = [int(i) for i in text]
max_summ = 0
k = 0
m = []
for j in range(len(nums)):
    if nums[j] % 10 == 0:
        m.append(nums[j])
for i in range(len(nums) - 1):
    if (nums[i] % 10 == nums[i + 1] % 10) and (((nums[i] % 7 == 0) and (nums[i + 1] % 7 != 0)) or ((nums[i] % 7 != 0) and (nums[i + 1] % 7 == 0))) and ((nums[i] ** 2 + nums[i + 1] ** 2) <= min(m) ** 2):
        k += 1
        max_summ = max(max_summ, nums[i] ** 2 + nums[i + 1] ** 2)
print(k, max_summ)
