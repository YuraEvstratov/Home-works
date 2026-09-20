text = open("/Users/yura/Downloads/17-5.txt")
nums = [int(i) for i in text]
max_summ = 0
k = 0
m = []
for j in range(len(nums)):
    if nums[j] % 10 == 5 and 99 < nums[j] < 1000:
        m.append(nums[j])
for i in range(len(nums) - 1):
    if (((999 < nums[i] < 10000) and not(999 < nums[i + 1] < 10000)) or ((999 < nums[i + 1] < 10000) and not(999 < nums[i] < 10000))) and ((nums[i] ** 2 + nums[i + 1] ** 2) % min(m) == 0):
        k += 1
        max_summ = max(max_summ, nums[i] ** 2 + nums[i + 1] ** 2)
print(k, max_summ)
