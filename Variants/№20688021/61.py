text = open("/Users/yura/Downloads/17-10.txt")
nums = [int(i) for i in text]
k = 0
max_summ = 0
l = []
for j in range(len(nums)):
    if nums[j] % 2 != 0:
        l.append(nums[j])
sr = sum(l) // len(l)
for i in range(len(nums) - 1):
    if (nums[i] % 5 == 0 and nums[i + 1] < sr) or (nums[i + 1] % 5 == 0 and nums[i] < sr):
        k += 1
        max_summ = max(max_summ, nums[i] + nums[i + 1])
print(k, max_summ)
