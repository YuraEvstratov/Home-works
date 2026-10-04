text = open("/Users/yura/Downloads/17-8.txt")
nums = [int(i) for i in text]
k = 0
max_sm = 0
a = []
for j in range(len(nums)):
    if nums[j] % 100 == 29:
        a.append(nums[j])
z = max(a)
for i in range(len(nums) - 2):
    if ((9999 < nums[i] < 100000 and 9999 < nums[i + 1] < 100000 and not(9999 < nums[i + 2] < 100000)) or (9999 < nums[i] < 100000 and not(9999 < nums[i + 1] < 100000) and 9999 < nums[i + 2] < 100000) or (not(9999 < nums[i] < 100000) and 9999 < nums[i + 1] < 100000 and 9999 < nums[i + 2] < 100000)) and ((nums[i] + nums[i + 1] + nums[i + 2]) <= z):
        k += 1
        max_sm = max(max_sm, nums[i] + nums[i + 1] + nums[i + 2])
print(k, max_sm)
