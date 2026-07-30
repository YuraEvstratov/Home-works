text = open("/Users/yura/Downloads/17-17.txt")
nums = [int(i) for i in text]
x = float("inf")
for j in range(len(nums)):
    if 99 < nums[j] < 1000 and nums[j] % 10 == 5:
        x = min(x, nums[j])
k = 0
min_sum = float("inf")
for i in range(len(nums) - 1):
    if  (((99 < nums[i] < 1000) and  not(99 < nums[i + 1] < 1000)) or (99 < nums[i + 1] < 1000) and  not(99 < nums[i] < 1000)) and ((nums[i] + nums[i + 1]) % x == 0):
        k += 1
        min_sum = min(min_sum, nums[i] + nums[i + 1] )
print(k, min_sum)
    