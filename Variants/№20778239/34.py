text = open("/Users/yura/Downloads/17-3.txt")
nums = [int(i) for i in text]
l = []
for j in range(len(nums)):
      if nums[j] % 2 != 0:
            l.append(nums[j])
max_sum, k = 0, 0
for i in range(len(nums) - 1):
        if (nums[i] % 5 == 0 and nums[i + 1] < sum(l)/len(l)) or (nums[i + 1] % 5 == 0 and nums[i] < sum(l)/len(l)):
            k += 1
            max_sum = max(max_sum, nums[i] + nums[i + 1] )
print(k, max_sum)