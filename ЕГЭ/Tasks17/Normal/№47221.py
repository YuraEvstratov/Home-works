text = open("/Users/yura/Downloads/17-8.txt")
nums = [int(i) for i in text]
k = 0
z = 0 
max_summ = 0
for i in range(len(nums)):
    if abs(nums[i]) % 10 == 3:
        z = max(z, nums[i])
for j in range(len(nums) - 1):
    if (nums[j] ** 2 + nums[j + 1] ** 2 >= z ** 2 and
        ((abs(nums[j]) % 10 == 3 and abs(nums[j + 1]) % 10 != 3) or
        (abs(nums[j]) % 10 != 3 and abs(nums[j + 1]) % 10 == 3))):
        k += 1
        max_summ = max(max_summ, nums[j] ** 2 + nums[j + 1] ** 2)
print(k, max_summ)
