text = open("/Users/yura/Downloads/17-7.txt")
nums = [int(i) for i in text]
k = 0
min_sm = float("inf")
a = []
for j in range(len(nums)):
    if nums[j] % 100 == 13:
        a.append(nums[j])
z = max(a)
for i in range(len(nums) - 2):
    if ((99 < nums[i] < 1000 and 99 < nums[i + 1] < 1000 and not(99 < nums[i + 2] < 1000)) or (99 < nums[i] < 1000 and not(99 < nums[i + 1] < 1000) and 99 < nums[i + 2] < 1000) or (not(99 < nums[i] < 1000) and 99 < nums[i + 1] < 1000 and 99 < nums[i + 2] < 1000)) and ((nums[i] + nums[i + 1] + nums[i + 2]) < z):
        min_sm = min(min_sm, nums[i] + nums[i + 1] + nums[i + 2])
        k += 1
print(k, min_sm)
