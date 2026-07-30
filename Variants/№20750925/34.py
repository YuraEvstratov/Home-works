text = open("/Users/yura/Downloads/17-8.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if abs(nums[j]) % 10 == 6:
        l.append(nums[j])
min_num = min(l) ** 2
k = 0
max_sum = 0
for i in range(len(nums) - 1):
    if (((abs(nums[i]) % 10 == 6 and abs(nums[i + 1]) % 10 != 6) or (abs(nums[i]) % 10 != 6 and abs(nums[i + 1]) % 10 == 6)) 
        and (abs((nums[i])) ** 2 + abs(nums[i + 1]) ** 2) < min_num):
        k += 1
        max_sum = max(nums[i] ** 2 + nums[i + 1] ** 2, max_sum) 
print(k, max_sum)
