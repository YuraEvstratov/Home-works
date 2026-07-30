text = open("/Users/yura/Downloads/17-5.txt")
nums = [int(i) for i in text]
k = 0
max_summ = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] - nums[j]) % 36 == 0 and (nums[i] % 13 == 0 or nums[j] % 13 == 0):
            k += 1
            max_summ = max(max_summ, nums[i] - nums[j])
print(k, max_summ)
