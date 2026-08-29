text = open("/Users/yura/Downloads/17-2.txt")
nums = [int(i) for i in text]
max_sum, k = 0, 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] * nums[j]) % 14 != 0 :
            k += 1
            max_sum = max(max_sum, nums[i] + nums[j] )
print(k, max_sum)