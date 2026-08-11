text = open("/Users/yura/Downloads/17-18.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
    if 99 < nums[j] < 1000 and nums[j] % 10 == 0:
        l.append(nums[j])
x = min(l)
k = 0
min_summ = float("inf")
for i in range(len(nums) - 1):
    if ((99 < nums[i] < 1000 != 99 < nums[i + 1] < 1000) or (99 < nums[i + 1] < 1000 != 99 < nums[i] < 1000)) and (nums[i] + nums[i + 1]) % x == 0 :
        k += 1
        min_summ = min(min_summ, nums[i] + nums[i + 1] )
print(k, min_summ)
