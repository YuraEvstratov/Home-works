text = open("/Users/yura/Downloads/17-3.txt")
nums = [int(i) for i in text]
k = 0
max_summ = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) % 2 != 0 and (nums[i] * nums[j]) % 3 == 0:
            k += 1
            max_summ = max(max_summ, nums[i] + nums[j])
print(k, max_summ)