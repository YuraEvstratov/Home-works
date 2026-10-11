text = open("/Users/yura/Downloads/17-2.txt")
nums = [int(i) for i in text]
k = max_sm = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] * nums[j] % 10 == 0:
            k += 1
            max_sm = max(max_sm, nums[i] + nums[j])
print(k, max_sm)
        