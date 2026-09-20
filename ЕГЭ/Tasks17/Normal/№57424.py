text = open("/Users/yura/Downloads/1_17.txt")
nums = [int(i) for i in text]
max_summ = 0
k = 0
m = []
for j in range(len(nums)):
    if 9 < nums[j] < 100:
        m.append(nums[j])
for i in range(len(nums) - 1):
    if (((9 < nums[i] < 100) and not(9 < nums[i + 1] < 100)) or ((9 < nums[i + 1] < 100) and not(9 < nums[i] < 100))) and ((nums[i] + nums[i + 1]) % max(m) == 0):
        k += 1
        max_summ = max(max_summ, nums[i]+ nums[i + 1])
print(k, max_summ)
