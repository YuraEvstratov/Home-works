text = open("/Users/yura/Downloads/17-10.txt")
nums = [int(i) for i in text]
l = []
for j in nums:
    if j % 2 == 0:
        l.append(j)
val = sum(l) // len(l)
k = 0
max_summa = 0
for i in range(len(nums) - 1):
    if (nums[i] % 3 == 0 and nums[i + 1] < val) or (nums[i + 1] % 3 == 0 and nums[i] < val):
        k += 1
        max_summa = max(max_summa, nums[i] + nums[i + 1])
print(k, max_summa)
