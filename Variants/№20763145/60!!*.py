text = open("/Users/yura/Downloads/17-13.txt")
nums = [int(i) for i in text]
l = []
m = min([i for i in nums if i % 100 == 99 and i >0])
for i in range(len(nums) - 2):
    tre = [nums[i], nums[i + 1], nums[i + 2]]
    abc = [j for j in tre if len(str(abs(j))) == 3]
    if len(abc) >= 2 and sum(tre) >= m:
        l.append(sum(tre))
print(len(l), min(l))
    