text = open("/Users/yura/Downloads/demo_2025_17.txt")
nums = [int(i) for i in text]
k = 0
max_summ = 0
z = min(nums)
for i in range(len(nums) - 1):
    if nums[i] % 16 == z or nums[i + 1] % 16 == z:
        k += 1
        max_summ = max(max_summ, nums[i] + nums[i + 1])
print(k, max_summ)