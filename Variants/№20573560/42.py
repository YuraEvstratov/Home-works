text = open("/Users/yura/Downloads/17-13.txt")
nums = [int(i) for i in text]
k = 0
min_summ = float("inf")
l = []
for i in range(len(nums)):
    if nums[i] > 0 and nums[i] % 100 == 77:
        l.append(nums[i])
z = min(l)
for i in range(len(nums) - 2):
    tre = [nums[i], nums[i + 1], nums[i + 2]]
    num = [x for x in tre if len(str(abs(x))) == 3]
    if len(num) < 2:
        if sum(tre) >= z:
            k += 1
            min_summ = min(min_summ, nums[i] + nums[i + 1] + nums[i + 2])
print(k, min_summ)