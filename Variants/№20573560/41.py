nums = open("/Users/yura/Downloads/17-12.txt").readline()
k = 0
l = []
min_summ = float("inf")
for j in range(len(nums)):
    if -999 > int(nums[j]) > -10000 and int(nums[j]) % 9 == 0:
        l.append(nums[j])
z = max(l)
for i in range(len(nums) - 1):
    if (((int(nums[i]) < 0 and int(nums[i + 1]) >= 0) or (int(nums[i]) > 0 and int(nums[i + 1]) <= 0)) and 
        int(nums[i]) + int(nums[i + 1]) > z):
        k += 1
        min_summ = min(min_summ, int(nums[i]) + int(nums[i + 1]))
print(k, min_summ)