text = open("/Users/yura/Downloads/17-8.txt")
nums = [int(i) for i in text]
l = []
k = 0 
max_summ = 0
for e in range(len(nums)):
    if nums[e] % 10 == "6":
        l.append(nums[e])
min_6 = min(l)
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[i] % 10 == "6" and nums[j] % 10 != "6" or nums[i] % 10 != "6" and nums[j] % 10 == "6" and (nums[i] ** 2 + nums[j] ** 2) < min_6 ** 2:
            k += 1
            max_summ = max(max_summ, nums[i] + nums[j])
print(k)
print(max_summ)