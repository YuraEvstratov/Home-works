text = open("/Users/yura/Downloads/17.txt")
nums = [int(i) for i in text]
k = 0
max_summ = 0
for i in range(len(nums) - 1):
    if nums[i] % 3 == 0 or nums[i + 1] % 3 == 0:
        k += 1
        max_summ = max(max_summ, nums[i] + nums[i + 1])
print(k, max_summ)