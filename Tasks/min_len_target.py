def min_len_target(nums:list, target:int) -> int:
    if not nums or not target:
         return False
    
    if target in nums:
        return 1

    r = 0
    l = 1
    while r != len(nums) - 1 and l != len(nums):
        if nums[r] + nums[l] == target:
                return 2
        if l == len(nums) - 1:
                r += 1
                l = r + 1
        l += 1

    t = -1
    global1 = []
    while t != len(nums) - 1:
        t += 1
        f = t + 1
        value = []
        value.append(nums[t])
        while f != len(nums):
            if sum(value) == target:
                global1.append(value)
                break
            value.append(nums[f])
            f += 1

    if not global1:
        return 0 
    return len(min(global1))
print(min_len_target([2,3,1,2,4,3],7))
print(min_len_target([1,4,4],4))
print(min_len_target([1,2,3,2],4))
print(min_len_target([1,1,1,1,1,1,1,1],11))