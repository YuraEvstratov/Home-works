text = open("/Users/yura/Downloads/17-10.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if abs(nums[j]) % 10 == 5:
        l.append(nums[j])
s = min(l)
k = 0
max_sm = 0
for i in range(len(nums) - 1):
    if abs(min(nums[i], nums[i + 1])) % 10 == 5 and ((nums[i] ** 2 + nums[i + 1] ** 2) < s ** 2):
        k += 1
        max_sm = max(max_sm, nums[i] ** 2 + nums[i + 1] ** 2)
print(k, max_sm)
