text = open("/Users/yura/Downloads/17-15.txt")
nums = [int(i) for i in text]
num = [str(i) for i in text]
maxx = max(nums)
minn = min(nums)
k = 0
summ = 0
for i in range(len(nums) - 2):
    if (((999 < nums[i] < 10000 and 999 < nums[i + 1] < 10000 and (nums[i + 2] < 1000 or nums[i + 2]> 9999)) or
        (999 < nums[i] < 10000 and 999 < nums[i + 2] < 10000 and (nums[i + 1] < 1000 or nums[i + 1]> 9999)) or
        (999 < nums[i + 2] < 10000 and 999 < nums[i + 1] < 10000 and (nums[i] < 1000 or nums[i]> 9999)) or
        (999 < nums[i] < 10000 and 999 < nums[i + 1] < 10000 and (nums[i + 2] < 1000 or nums[i + 2]> 9999)) or 
        (999 < nums[i + 2] < 10000 and 999 < nums[i] < 10000 and (nums[i + 1] < 1000 or nums[i + 1]> 9999)) or
        (999 < nums[i] < 10000 and 999 < nums[i + 2] < 10000 and (nums[i + 1] < 1000 or nums[i + 1]> 9999))) and
        ((num[i][-1] == maxx[-1]) or(num[i + 1][-1] == maxx[-1])or (num[i+ 2][-1] == maxx[-1])) and
        ((num[i][-1] != minn[-1]) or(num[i + 1][-1] != minn[-1])or (num[i+ 2][-1] != minn[-1]))):
        k += 1
        summ = max(summ, nums[i] + nums[i + 1] + nums[i + 2])
print(k, summ)