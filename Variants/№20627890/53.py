text = open("/Users/yura/Downloads/17-2.txt")
nums = [int(i) for i in text]
max_summ = 0
k = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] * nums[j]) % 34 != 0:
            max_summ = max(max_summ, nums[i] + nums[j])
            k += 1
print(k, max_summ)