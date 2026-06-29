text = open("/Users/yura/Downloads/1_17.txt")
nums = [int(i) for i in text]
k = 0
max_summ = 0
max_value = 0
for j in range(len(nums)):
    if 9 < nums[j] < 100:
        max_value = max(max_value, nums[j])
for i in range(len(nums) - 1):
    if (((9 < nums[i] < 100) != (9 < nums[i + 1] < 100))  and 
        ((nums[i] + nums[i + 1]) % max_value == 0)):
        k += 1
        max_summ = max(max_summ, nums[i] + nums[i + 1])
print(k, max_summ)
