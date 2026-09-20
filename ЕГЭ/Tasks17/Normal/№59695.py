text = open("/Users/yura/Downloads/17-6.txt")
nums = [int(i) for i in text]
max_summ = 0
k = 0
m = []
for j in range(len(nums)):
    if nums[j] % 100 == 15:
        m.append(nums[j])
for i in range(len(nums) - 2):
    if (((999 < nums[i] < 10000) and not(999 < nums[i + 1] < 10000) and not(999 < nums[i + 2] < 10000)) or ((999 < nums[i + 1] < 10000) and not(999 < nums[i] < 10000) and not(999 < nums[i + 2] < 10000)) or ((999 < nums[i + 2] < 10000) and not(999 < nums[i + 1] < 10000) and not(999 < nums[i] < 10000))) and ((nums[i] + nums[i + 1] + nums[i + 2]) >= max(m)):
        k += 1
        max_summ = max(max_summ, nums[i] + nums[i + 1] + nums[i + 2])
print(k, max_summ)
