text = open("/Users/yura/Downloads/17.txt")
max_summ = 0
k = 0
nums = [int(i) for i in text]
for i in range(len(nums) - 1):
    if nums[i] % 3 == 0 or nums[i + 1] % 3 == 0:
        k += 1
        max_summ = max(max_summ, int(nums[i]) + int(nums[i + 1]))
print(k, max_summ)