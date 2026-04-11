def min_len_target(nums: list, target: int) -> int:
    if not nums or not target:
         return False

    left = 0
    summ = 0
    min_len = float("inf")
    for right in range(len(nums)):
        summ += nums[right]

        while summ >= target:
            min_len = min(right - left + 1, min_len)
            summ -= nums[left]
            left += 1

    return min_len if min_len < float("inf") else 0

print(min_len_target([2,3,1,2,4,3],7))
print(min_len_target([1,4,4],4))
print(min_len_target([1,2,3,2],4))
print(min_len_target([1,1,1,1,1,1,1,1],11))