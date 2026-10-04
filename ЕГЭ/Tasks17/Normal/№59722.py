text = open("/Users/yura/Downloads/1_17.txt")
nums = [int(i) for i in text]
k = 0
a = []
for j in range(len(nums)):
    if nums[j] % 100 == 17:
        a.append(nums[j])
z = max(a)
for i in range(len(nums) - 2):
    if  ((99 < nums[i] < 1000 and not(99 < nums[i + 1] < 1000) and not(99 < nums[i + 2] < 1000)) or (99 < nums[i + 1] < 1000 and not(99 < nums[i] < 1000) and not(99 < nums[i + 2] < 1000)) or (99 < nums[i + 2] < 1000 and not(99 < nums[i + 1] < 1000) and not(99 < nums[i] < 1000))) and ((nums[i] + nums[i + 1] + nums[i + 2]) < z):
        k += 1
print(k)
