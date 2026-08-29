text = open("/Users/yura/Downloads/17-4.txt")
nums = [int(i) for i in text]
l = -10000001
for j in range(len(nums)):
      if nums[j] % 10 == 3:
            l = max(l, nums[j])
max_sum, k = 0, 0
for i in range(len(nums) - 1):
        if ((nums[i] % 10 == 3 and nums[i + 1] % 10 != 3) or (nums[i + 1] % 10 == 3 and nums[i] % 10 != 3)) and (nums[i] ** 2 + nums[i + 1] ** 2) >= l ** 2:
            k += 1
            max_sum = max(max_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(k, max_sum)