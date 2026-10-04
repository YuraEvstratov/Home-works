text = open("/Users/yura/Downloads/17-7.txt")
nums = [int(i) for i in text]
k = 0
min_sm = float("inf")
a = []
for j in range(len(nums)):
    if nums[j] % 100 == 15:
        a.append(nums[j])
z = max(a)
for i in range(len(nums) - 2):
    if  ((999 < nums[i] < 10000 and not(999 < nums[i + 1] < 10000) and not(999 < nums[i + 2] < 10000)) or (999 < nums[i + 1] < 10000 and not(999 < nums[i] < 10000) and not(999 < nums[i + 2] < 10000)) or (999 < nums[i + 2] < 1000 and not(999 < nums[i + 1] < 10000) and not(999 < nums[i] < 10000))) and ((nums[i] + nums[i + 1] + nums[i + 2]) < z):
        k += 1
        min_sm = min(min_sm, nums[i] + nums[i + 1] + nums[i + 2])
print(k, min_sm)